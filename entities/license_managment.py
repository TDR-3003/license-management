from pony.orm import Required, Optional, PrimaryKey, Set, perm
from config import db


class Users(db.Entity):
    id_user = PrimaryKey(int, auto=True)
    name = Required(str, 50)
    last_name = Required(str, 50)
    email = Required(str, 50)
    password = Required(str, 250)
    status = Required(int)


db.generate_mapping(create_tables=True, check_tables=True)
