from app.database.orm.model import Model
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
    def get_all():
        """Gets all the rows in Model.
        
        .. versionchanged:: 0.1
        """
        return Model.query.all()
