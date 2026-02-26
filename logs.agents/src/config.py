from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(Path(__file__).parent.parent / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DETECTOR_MODEL = "gpt-4o"
ANIMATOR_MODEL = "gpt-4o"
CRITIC_MODEL   = "gpt-4o"

MAX_ITER    = 4
PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
OUTPUTS_DIR = Path(__file__).parent.parent / "outputs"
FIGURES_DIR = Path(__file__).parent.parent / "figures"