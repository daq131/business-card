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
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address})"

    @property
    def contact_phone(self):
        return f"Choose work phone: {self.tel_work} and call to {self.first_name} {self.last_name}"

    @contact_phone.setter
    def contact_phone(self, value):
            self.tel_work = value

    def contact(self, *args):
        return f"CCCChoose home phone: {self.tel_priv} and call to {self.first_name} {self.last_name} "

    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name)])


class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation
        super().contact_phone

human_1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())

print(human_1)
print(human_1.contact())
print(human_1.contact_phone)
print(BusinessContact.contact_phone)

def create_contacts(kind, how_many):
    business_card2 = []
    for i in range(how_many):
        if kind == 'b':
            company =  business_card2.append(fake.company()),
            tel_work = business_card2.append(fake.phone_number()),
            occupation = business_card2.append(fake.job()),
            tel_work = business_card2.append(fake.phone_number()),
        elif kind == 'h':
            first_name = business_card2.append(fake.name()),
            last_name = business_card2.append(fake.last_name()),
            email_address = business_card2.append(fake.email()),
            tel_priv = business_card2.append(fake.phone_number())
    return business_card2


if __name__ == "__main__":
    kind = input("select the type of business card: b - business, h - home: ")
    how_many = int(input('please select number of cards '))
    cards = create_contacts(kind, how_many)
    print(cards)