import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concession_api.settings')
django.setup()

from gestion_concessions.models import Concession, Vehicule

faker = Faker('fr_FR')

def create_concessions_and_vehicles(concessions_count=10, vehicles_per_concession=5):
    print("Création des concessions et des véhicules...")
    for _ in range(concessions_count):
        concession = Concession.objects.create(
            nom=faker.company(),
            numero_siret=random.randint(10000000000000, 99999999999999),
            code_postal=faker.postcode(),
            adresse=faker.address()
        )

        for _ in range(vehicles_per_concession):
            Vehicule.objects.create(
                marque=faker.company(),
                modele=faker.word().capitalize(),
                chevaux=random.randint(50, 400),
                immatriculation=faker.license_plate(),
                date_mise_en_service=faker.date_this_century(before_today=True, after_today=False),
                concession=concession
            )
    print("Données générées avec succès.")

if __name__ == '__main__':
    create_concessions_and_vehicles()
