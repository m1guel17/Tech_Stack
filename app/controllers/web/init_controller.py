from flask import render_template
# from app.database.orm import *
from app.database.services import ModelServices
from app import db

def initialRoutes(app):
    @app.route('/')
    def index():
        all = ModelServices.get_all()
            
        return render_template('index.html', all=all)
    
    @app.route('/tables')
    def tables():
        tables_info = {}
        for table_name, table in db.metadata.tables.items():
            columns = [{
                "name": column.name,
                "type": str(column.type),
                "nullable": column.nullable,
                "primary_key": column.primary_key
            } for column in table.columns]
            tables_info[table_name] = columns
            
        return render_template('all_tables.html', tables_info=tables_info)

    