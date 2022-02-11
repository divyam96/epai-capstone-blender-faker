from faker import Faker
import pickle

NUMBER_OF_SAMPLES = 200


Faker.seed(0)
fake = Faker()

faker_dict ={'phone_numbers': [],
             'rgb_colors': [],
             'barcodes': [],
             'persons': [],
             'automotive_license_plates': [],
             'lat_longs': [],
             'credit_card_details': [],
             'companies': [],
             'email_ids': [],
             'user_agents': []}

# Phone Numbers
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['phone_numbers'].append(fake.phone_number())

# RGB Colors
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['rgb_colors'].append(fake.rgb_color())

# Barcodes
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['barcodes'].append(fake.ean(length=13))

# Persons
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['persons'].append(fake.name())

# Automotive Licenses
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['automotive_license_plates'].append(fake.license_plate())

# Lat Longs
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['lat_longs'].append(fake.local_latlng())


# Credit Details
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['credit_card_details'].append(fake.credit_card_full())

# Companies
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['companies'].append(fake.company())

# Email-ids
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['email_ids'].append(fake.ascii_email())

# User Agents
for _ in range(NUMBER_OF_SAMPLES):
   faker_dict['user_agents'].append(fake.user_agent())

# print(faker_dict.keys())

with open('faker_data_dump.pickle', 'wb') as handle:
    pickle.dump(faker_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

