from application import app, db
from application.models import IncomeExpenses

# Establece un contexto de aplicación
if __name__ == '__main__':
    with app.app_context():
        # Crea todas las tablas de la base de datos
        db.create_all()
