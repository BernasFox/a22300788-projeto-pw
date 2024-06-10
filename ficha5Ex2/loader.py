from ficha5Ex2.models import *
import json

def load_bandas_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for banda_data in data['bandas']:
            banda, created = Banda.objects.get_or_create(
                nome=banda_data['nome'],
                ano_criacao=banda_data['ano_criacao'],
                nacionalidade=banda_data['nacionalidade']
            )

def load_discos_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for disco_data in data['discos']:
            banda_obj = Banda.objects.get(nome=disco_data['banda'])
            disco, created = Disco.objects.get_or_create(
                banda=banda_obj,
                titulo=disco_data['titulo'],
                ano_lancamento=disco_data['ano_lancamento']
            )
            for musica_data in disco_data['musicas']:
                Musica.objects.create(
                    disco=disco,
                    titulo=musica_data['titulo'],
                    duracao=musica_data['duracao']
                )


load_bandas_from_json('ficha5Ex2/Json/Bandas.json')
load_discos_from_json('ficha5Ex2/Json/Discos.json')
