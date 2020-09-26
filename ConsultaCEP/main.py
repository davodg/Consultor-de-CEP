import requests


def consultar():

    print('############################################')
    print('###Bem vindo ao painel de consulta de CEP###')
    print('############################################')

    cep_input = input('Digite o CEP que deseja consultar: ')

    if len(cep_input) != 8:
        print('Quantidade de números do CEP inválida.')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('CEP encontrado!!')
        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
        print('DDD: {}'.format(address_data['ddd']))
    else:
        print('{} é um cep inválido.'.format(cep_input))

    repeat = int(input('Deseja realizar uma nova consulta?\n1.Sim\n2.Não\n'))

    if repeat == 1:
        consultar()
    else:
        print('Obrigado por utilizar nosso sistema...')


consultar()
