from enum import Enum

class DaysOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @staticmethod
    def get_name_day(number: int):
        if number < 1 or number > 7:
            print('Enter a number between 1 and 7')
        else:
            name_day = DaysOfWeek(number).name.capitalize()
            return print(f'The name of the day {number} is {name_day}')

# number = int(input('Enter a number from 1 to 7: '))
# name = DaysOfWeek.get_name_day(number)

# extra

class Status(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

class Order:
    def __init__(self, id_order):
        self.id_order = id_order
        self.status = Status.PENDING

    def status_name(self):
        status_names = {
            Status.PENDING: 'Pending',
            Status.SHIPPED: 'Shipped',
            Status.DELIVERED: 'Delivered',
            Status.CANCELLED: 'Cancelled'
        }
        return status_names.get(self.status, 'Unknown')

    def send_order(self):
        if self.status == Status.PENDING:
            self.status = Status.SHIPPED
            print(f'Order {self.id_order} was shipped')
        else:
            print(f'Order {self.id_order} cannot be shipped because its status is {self.status_name()}')

    def cancel_order(self):
        if self.status == Status.SHIPPED or self.status == Status.PENDING:
            self.status = Status.CANCELLED
            print(f'Order {self.id_order} has been canceled')
        else:
            print(f'Order {self.id_order} cannot bt canceled because its status is {self.status_name()}')
    
    def deliver_order(self):
        if self.status == Status.SHIPPED:
            self.status = Status.DELIVERED
            print(f'Order {self.id_order} has been delivered')
        else:
            print(f'Order {self.id_order} cannot bt delivered because its status is {self.status_name()}')
    
    def show_order(self):
        print(f'Order {self.id_order} has status {self.status_name()}')
    
order1 = Order("Tequeños")
order1.show_order()
order1.send_order()
order1.deliver_order()


order2 = Order("Pastelitos")
order2.show_order()
order2.send_order()
order2.cancel_order()
