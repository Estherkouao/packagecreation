import os
import shutil
import sys

def create_app():
    if len(sys.argv) < 2:
        print("Usage: python -m useapp.generate utiliseapp")
        return

    app_name = sys.argv[1]
    current_dir = os.getcwd()
    template_dir = os.path.join(os.path.dirname(__file__), 'templates', 'utiliseapp')
    target_dir = os.path.join(current_dir, app_name)

    if os.path.exists(target_dir):
        print(f"L'application '{app_name}' existe déjà.")
        return

    shutil.copytree(template_dir, target_dir)
    print(f"✅ Application '{app_name}' créée avec succès dans {current_dir}.")

if __name__ == "__main__":
    create_app()
