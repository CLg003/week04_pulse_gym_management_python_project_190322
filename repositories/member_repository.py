from logging.handlers import MemoryHandler
from db.run_sql import run_sql

from models.member import Member
from models.fitness_class import FitnessClass
from models.booking import Booking

def save(member):
    sql = "INSERT INTO members (first_name, last_name, address, email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.address, member.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member