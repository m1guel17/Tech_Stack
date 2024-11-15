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
    def by(id, **kwargs):
        """Updates Model entry for the specified id.
        
        :param id: String variable used to update Model instance
        :param **kwargs: Fields to update on the Model instance
        
        .. versionchanged:: 0.1
        """
        modelInstance = Model.query.filter_by(id=id).first()
        
        if modelInstance is not None:
            for key, value in kwargs.items():
                setattr(modelInstance, key, value)
            db.session.commit()