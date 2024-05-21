import shutil
import os

def delete_pycache(directory):
    """
    Function delete_pycache.

    ## Descrição:
    Criado apenas para deletar o tão chato e insuportável `pycache`.
    """
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))