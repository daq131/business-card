from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, email_address, tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_priv = tel_priv

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.tel_priv}"
    # print(people_1)
    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address}, tel_priv={self.tel_priv})"

    @property
    def contact_phone(self):
        return self.tel_priv

    def contact(self):
        return f"Contact: {self.first_name} at {self.contact_phone}"

    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name)])


class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation


    def __str__(self):
        return f"{self.tel_work}, {self.company}, {self.occupation}"

    @property
    def contact_phone(self):
        return self.tel_work

# human_1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
#               email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())

h1 = BaseContact("Dawid", "Szarwark", "dsz@email.com", "943165432")
h2 = BaseContact("Zenek", "Lubek", "zb@email.com", "945692321")
b1 = BusinessContact("11111321", "Dgsm", "webmaster", "Szefoo", "Zgredek", "zd@email.com", "33333333")

def create_contacts(kind, how_many):
    business_card2 = []
    for i in range(how_many):
        if kind == 'b':
            business_card2.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(),
                                             tel_priv=fake.phone_number(), tel_work=fake.phone_number(), company=fake.company(), occupation=fake.job()))
        elif kind == 'h':
            business_card2.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(), tel_priv=fake.phone_number()))

    return business_card2

if __name__ == "__main__":
    kind = input("select the type of business card: b - business, h - home: ")
    how_many = int(input('please select number of cards '))
    cards = create_contacts(kind, how_many)
    for i in cards:
        print(i)