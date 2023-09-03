import os
import subprocess


def generate_requirements():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    src_path = os.path.join(base_dir, "../src")
    requirements_path = os.path.join(base_dir, "../requirements.txt")

    try:
        subprocess.check_call(
            ["pipreqs", "--force", "--savepath", requirements_path, src_path]
        )
    except subprocess.CalledProcessError as e:
        print("Failed to generate requirements.txt")
        print(str(e))


if __name__ == "__main__":
    generate_requirements()
