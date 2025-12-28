from PIL import Image, ImageSequence
import os

def create_fadein_gif(input_path, output_path, n_frames=6, duration=120):
    img = Image.open(input_path).convert('RGB')
    frames = []
    for i in range(1, n_frames + 1):
        alpha = i / n_frames
        white = Image.new('RGB', img.size, (255, 255, 255))
        blended = Image.blend(white, img, alpha)
        frames.append(blended)
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True)

if __name__ == "__main__":
    input_img = "figures/homography/fig_matching_two_images3.png"
    output_gif = "figures/homography/fig_matching_two_images3.gif"
    create_fadein_gif(input_img, output_gif)
    print(f"Saved fade-in GIF: {output_gif}")
