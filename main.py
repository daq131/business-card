from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, first_name, last_name, email_address, tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_priv = tel_priv

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.occupation}, {self.company}"
    # print(people_1)
    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address})"

    def contact(self):
        return f"Choose home phone: {self.tel_priv} and call to {self.first_name} {self.last_name} "

    def workcontact(self):
        return f"Choose work phone: {self.tel_work} and call to {self.first_name} {self.last_name}"

    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name), +1])

class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation

def create_contacts(kind, how_many):
    contacts = []
    for i in range(how_many):
        if kind == 'b':
            contacts.append(BusinessContact)
        elif kind == 'h':
            contacts.append(BaseContact)
    return contacts

if __name__ == "__main__":
    kind = input("select the type of business card: b - business, h - home: ")
    how_many = int(input('please select number of cards '))
    cards = create_contacts(kind, how_many)
    # print(cards)