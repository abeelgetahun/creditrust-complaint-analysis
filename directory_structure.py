import os
from pathlib import Path

def create_folder_structure(base_path):
    """Create the folder structure for the creditrust-complaint-analysis project."""
    
    # Root directory files
    root_files = [
        'README.md',
        'requirements.txt',
        '.gitignore',
        'app.py'
    ]
    
    # Directories and their contents
    dir_structure = {
        'config': ['config.yaml'],
        'data': {
            'raw': [],
            'processed': [],
            'filtered_complaints.csv': None
        },
        'notebooks': [
            '01_exploratory_data_analysis.ipynb',
            '02_embedding_and_indexing.ipynb'
        ],
        'src': [
            '__init__.py',
            'data_preprocessing.py',
            'text_processing.py',
            'embedding_utils.py',
            'rag_pipeline.py'
        ],
        'vector_store': [],
        'models': [],
        'reports': ['interim_report.md']
    }
    
    # Create base directory
    base_path = Path(base_path)
    base_path.mkdir(exist_ok=True)
    print(f"Created base directory: {base_path}")
    
    # Create root files
    for file in root_files:
        file_path = base_path / file
        file_path.touch()
        print(f"Created file: {file_path}")
    
    # Create directories and their contents
    for dir_name, contents in dir_structure.items():
        dir_path = base_path / dir_name
        
        if isinstance(contents, dict):
            # Handle nested directory structure (like the data directory)
            dir_path.mkdir(exist_ok=True)
            print(f"Created directory: {dir_path}")
            
            for subdir_name, subcontents in contents.items():
                subdir_path = dir_path / subdir_name
                if subcontents is None:
                    # It's a file
                    subdir_path.touch()
                    print(f"Created file: {subdir_path}")
                else:
                    # It's a directory
                    subdir_path.mkdir(exist_ok=True)
                    print(f"Created directory: {subdir_path}")
                    
                    # Create files in this subdirectory if specified
                    for item in subcontents:
                        item_path = subdir_path / item
                        item_path.touch()
                        print(f"Created file: {item_path}")
        else:
            # Handle simple directories
            dir_path.mkdir(exist_ok=True)
            print(f"Created directory: {dir_path}")
            
            # Create files in this directory
            for item in contents:
                item_path = dir_path / item
                item_path.touch()
                print(f"Created file: {item_path}")

if __name__ == "__main__":
    project_path = "creditrust-complaint-analysis"
    create_folder_structure(project_path)
    print("\nFolder structure created successfully!")