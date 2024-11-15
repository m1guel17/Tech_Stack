from app.interfaces.crud.create.model_repo import ModelRepository as Create
from app.interfaces.crud.read.model_repo import ModelRepository as Read
from app.interfaces.crud.update.model_repo import ModelRepository as Update
from app.interfaces.crud.delete.model_repo import ModelRepository as Delete

"""
    CURRENT_DIRECTORY - CURRENT_FILENAME script to (...insert the use for this script)
    ----------------------------------------------------------------------------
    >Created: 2024-11-04
    >Last_modified: 2024-11-04
    >Author: Miguel
"""

class Model:
    # ================================= CREATE =================================
    @staticmethod
    def register(phone_number: str):        
        Create.new(phone_number)
    
    # ================================== READ ==================================
    @staticmethod
    def get_all():
        return Read.get_all()
    
    # ================================= UPDATE =================================
    @staticmethod
    def update_status(id: str, status_update: str):
        Update.by(id, status=status_update)
    
    # ================================= DELETE =================================
    @staticmethod
    def delete(id: str):
        Delete.by(id)
    