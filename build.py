import os
import subprocess
import sys
import shutil
from pathlib import Path

def create_venv():
    """Create a virtual environment if it doesn't exist"""
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)

def install_requirements():
    """Install packages from requirements.txt in the virtual environment"""
    # Get the correct pip path based on OS
    pip_cmd = 'venv/bin/pip' if os.name != 'nt' else r'venv\Scripts\pip'
    
    print("Installing requirements...")
    subprocess.run([pip_cmd, 'install', '-r', 'requirements.txt'], check=True)

def clean_output():
    """Clean up previous build artifacts"""
    output_dir = Path('_output')
    if output_dir.exists():
        print("Cleaning up previous build...")
        shutil.rmtree(output_dir)
    dist_dir = Path('dist')
    if output_dir.exists():
        print("Cleaning up previous build...")
        shutil.rmtree(dist_dir)
    # Just create _output, let JupyterLite handle its internal structure
    output_dir.mkdir(exist_ok=True)

def create_wheel():
    """Create a wheel package for vincent"""
    print("Creating wheel package...")
    # First ensure wheel is installed
    pip_cmd = 'venv/bin/pip' if os.name != 'nt' else r'venv\Scripts\pip'
    subprocess.run([pip_cmd, 'install', 'wheel', 'setuptools'], check=True)
    
    # Create wheels directory for explicit wheels
    wheels_dir = 'wheels'
    if not os.path.exists(wheels_dir):
        os.makedirs(wheels_dir)
    
    # Build the wheel in wheels directory
    pip_cmd = 'venv/bin/python' if os.name != 'nt' else r'venv\Scripts\python'
    subprocess.run([
        pip_cmd,  # Use venv python instead of sys.executable
        'setup.py', 
        'bdist_wheel', 
        '-d', 
        wheels_dir
    ], check=True)
    
    wheels = [f for f in os.listdir(wheels_dir) if f.endswith('.whl')]
    if wheels:
        print(f"Created wheels: {wheels}")

def run_jupyter_lite():
    """Run jupyter lite build command"""
    print("Building JupyterLite site...")
    
    python_cmd = 'venv/bin/python' if os.name != 'nt' else r'venv\Scripts\python'
    subprocess.run([
        python_cmd,
        '-m',
        'jupyter',
        'lite',
        'build'
    ], check=True)

def post_build_script():
    """Run post build script"""
    print("Running post build script...")
    python_cmd = 'venv/bin/python' if os.name != 'nt' else r'venv\Scripts\python'
    subprocess.run([python_cmd, 'post-build.py'], check=True)

def main():
    try:
        create_venv()
        install_requirements()  # This installs requirements.txt
        clean_output()
        create_wheel()         # Now wheel package is available
        run_jupyter_lite()
        post_build_script()
        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during build process: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
