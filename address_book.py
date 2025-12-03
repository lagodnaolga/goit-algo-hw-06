from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, phone_input):
        if not self.is_phone_valid(phone_input):
            raise ValueError("Incorrect phone format.")

        super().__init__(phone_input)
    
    def is_phone_valid(self, phone_to_validate):
        len_condition = len(phone_to_validate)==10
        format_condition = phone_to_validate.isdigit()
        return len_condition and format_condition

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_to_add):
        self.phones.append(Phone(phone_to_add))

    def remove_phone(self, phone_to_be_removed):
        phone = self.find_phone (phone_to_be_removed)
        if phone is None:
            raise ValueError("Phone is not found.")
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone is None:
            raise ValueError("Phone is not found.")
        if phone.is_phone_valid(new_phone):
            phone.value = new_phone
        else:
            raise ValueError("Incorrect phone format.")

    
    def find_phone (self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    #додає до AddressBook екземпляри класу Record {record.name.value: record}

    def add_record (self, record):
        self.data[record.name.value] = record

    def find (self, record_to_find):
        return self.data.get(record_to_find) 

    def delete (self, record_to_delete):
        if record_to_delete in self.data:
            del self.data[record_to_delete]
        return
    
    def __str__(self):
        result = ""
        for record in self.data.values():
            result += str(record) + "\n"
        return result





book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.edit_phone("5555555555", "5555555558")
book.add_record(john_record)
book.find("John")


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print (book)