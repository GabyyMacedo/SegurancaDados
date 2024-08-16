pessoas=[
    {
        "nome":"Igor",
        "idade":20,
        "prontuario":"sp12345",
        "notas":{
        "portugues":6,
        "matematica":8,
        "ciencias":10,
        "media": (10+6+8)/3,
        }
    },

    {
        "nome":"Ana",
        "idade":19,
        "prontuario":"sp45678",
        "notas":{
        "portugues":10,
        "matematica":3,
        "ciencias":9,
        "media": (10+3+9)/3,
        }
    }
]
def get_pessoas():
    return pessoas

print(get_pessoas())