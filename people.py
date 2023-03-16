from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Martins": {
        "fname": "Diana",
        "lname": "Martins",
        "evento": "Aula de Modelagem",
        "timestamp": get_timestamp(),
    },
    "Daniel": {
        "fname": "Júlio",
        "lname": "Daniel",
        "evento": "Encontro com Amigos",
        "timestamp": get_timestamp(),
    },
    "Catarine": {
        "fname": "Flávia",
        "lname": "Catarine",
        "evento": "Coffeetalk",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    return list(PEOPLE.values())


def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(406, f"Pessoa com sobrenome {lname} já existe")


def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(404, f"Pessoa com sobrenome {lname} não encontrada")


def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, f"Pessoa com sobrenome {lname} não encontrada")


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"{lname} foi deletado", 200)
    else:
        abort(404, f"Pessoa com sobrenome {lname} não encontrada")
