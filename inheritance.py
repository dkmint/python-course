class NewSensor(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand
        
        
new_sensor = NewSensor('OK', 'SF', '2019-01-01', 'XYZ')
new_sensor.brand
