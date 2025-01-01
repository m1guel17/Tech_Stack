from app.database.orm.model import ModelBuilder
from app import db

"""
    CRUD -> {OPERATOR} CURRENT_FILENAME script to (...insert the use for this script)
    ----------------------------------------------------------------------------
    >Created: 2024-11-04
    >Last_modified: 2024-12-31
    >Points: Services
    >Author: Miguel
"""

class ModelRepository:
    @staticmethod
    def new(phone_number: str):
        """Stores client phone_number into Model.
        
        :param phone_number: String variable used to store in Model

        .. versionchanged:: 1.0
        """
        modelInstance = ModelBuilder().set_phone_number(phone_number).build()
        
        db.session.add(modelInstance)
        db.session.commit()
        