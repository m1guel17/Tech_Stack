from app.models.orm.model import Model
from app import db

"""
    CRUD -> {OPERATOR} CURRENT_FILENAME script to (...insert the use for this script)
    ----------------------------------------------------------------------------
    >Created: 2024-11-04
    >Last_modified: 2024-11-04
    >Author: Miguel
"""

class ModelRepository:
    @staticmethod
    def new(phone_number: str):
        """Stores client phone_number into Model.
        
        :param phone_number: String variable used to store in Model the phone_number.

        .. versionchanged:: 0.1
        """
        clientInstance = Model(phone_number=phone_number)
        
        db.session.add(clientInstance)
        db.session.commit()
        