from app.database.CRUD.create.model_repo import ModelRepository as Create
from app.database.CRUD.read.model_repo   import ModelRepository as Read
from app.database.CRUD.update.model_repo import ModelRepository as Update
from app.database.CRUD.delete.model_repo import ModelRepository as Delete

"""
    CURRENT_DIRECTORY - CURRENT_FILENAME script to (...insert the use for this script)
    ----------------------------------------------------------------------------
    >Created: 2024-11-04
    >Last_modified: 2024-12-31
    >Author: Miguel
"""

class ModelServices:
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
    def update_status(id: str, string: str):
        Update.byId(id, string=string)
    
    # ================================= DELETE =================================
    @staticmethod
    def delete(id: str):
        Delete.byId(id)
    