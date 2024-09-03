import os
import re

def extract_latex_figures(latex_content):
    figures = {}
    figure_pattern = re.compile(
        r'\\begin{figure}.*?\\includegraphics\[width=(.*?)\]\{(.*?)\}.*?\\caption\{(.*?)\}.*?\\label\{(.*?)\}.*?\\end{figure}',
        re.S
    )
    matches = figure_pattern.findall(latex_content)
    
    for width, image_path, caption, label in matches:
        figures[label] = {
            "image_path": image_path.strip(),
            "caption": caption.strip(),
            "width": width.strip() if width else None,
        }
    
    return figures

def convert_width_to_percentage(width_value):
    """Converts LaTeX width format (.8, .7) to Quarto format (80%, 70%)."""
    match = re.match(r'\.([\d]+)', width_value)
    if match:
        percentage = f'{int(match.group(1)) * 10}%'
        return percentage
    return width_value

def update_qmd_with_labels_captions(latex_figures, qmd_content):
    for label, details in latex_figures.items():
        image_name_base = details["image_path"].split("/")[-1].rsplit('.', 1)[0]  # Get the base name without extension
        image_pattern = re.compile(rf'!\[\]\((.*?/{image_name_base}\.(?:png|jpg|jpeg|pdf))\)\{{(.*?)\}}')
        match = image_pattern.search(qmd_content)
        if match:
            image_line = match.group(0)
            current_attributes = match.group(2).strip()

            # Check and update width if it's missing or needs conversion
            if details["width"]:
                converted_width = convert_width_to_percentage(details["width"])
                width_pattern = re.compile(r'width\s*=\s*"?[\d.]+%?"?')
                if width_pattern.search(current_attributes):
                    # Replace existing width
                    current_attributes = width_pattern.sub(f'width="{converted_width}"', current_attributes)
                else:
                    # Add the width if not present
                    current_attributes += f' width="{converted_width}"'

            # Append the label to the existing attributes
            label_to_add = f"#{label.replace(':', '-')}"
            if label_to_add not in current_attributes:
                new_attributes = f"{current_attributes} {label_to_add}"
                new_image_line = f'![{details["caption"]}]({match.group(1)}){{{new_attributes}}}'
                qmd_content = qmd_content.replace(image_line, new_image_line)
    
    return qmd_content

def compare_and_update_figures(latex_file, qmd_file, output_file):
    with open(latex_file, 'r') as f:
        latex_content = f.read()
    
    with open(qmd_file, 'r') as f:
        qmd_content = f.read()

    latex_figures = extract_latex_figures(latex_content)
    
    updated_qmd_content = update_qmd_with_labels_captions(latex_figures, qmd_content)
    
    with open(output_file, 'w') as f:
        f.write(updated_qmd_content)

def find_latex_file(root_dir, qmd_filename):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file == qmd_filename.replace('.qmd', '.tex'):
                return os.path.join(subdir, file)
    return None

def process_all_qmd_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.qmd'):
                qmd_file = os.path.join(subdir, file)
                latex_file = find_latex_file(root_dir, file)
                if latex_file:
                    output_file = qmd_file  # Overwrite the original .qmd file
                    compare_and_update_figures(latex_file, qmd_file, output_file)
                    print(f"Processed: {qmd_file}")
                else:
                    print(f"No corresponding LaTeX file found for: {qmd_file}")

# Determine the grandparent directory as the root directory
current_script_directory = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.abspath(os.path.join(current_script_directory, os.pardir, os.pardir))

# Run the script
process_all_qmd_files(root_directory)