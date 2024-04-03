from datetime import datetime, timedelta

class fechas:
    def fechaActual(self):
        today = datetime.now()
        format = today.strftime('Fecha: %d/%m/%Y, hora: %H:%M:%S')
        return format

    def mi_nacimiento(self):
        birthdate = datetime(1998, 10, 13)
        format = birthdate.strftime('%d/%m/%Y')
        current = datetime.now()
        current_adjusted = current - timedelta(hours=2, minutes=13)
        format_current = current_adjusted.strftime('%H:%M:%S')
        return (f"Mi nacimiento: {format} a las {format_current}")
    
fecha = fechas()
print(fecha.fechaActual())
print(fecha.mi_nacimiento())