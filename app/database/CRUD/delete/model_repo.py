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
    def byId(id: str):
        """Deletes instace from Model by id.
        
        :param id: Integer variable used to locate Model instance to delete.

        .. versionchanged:: 0.1
        """
        modelInstance = Model.query.filter_by(id=id).first()
        db.session.delete(modelInstance)
        db.session.commit()