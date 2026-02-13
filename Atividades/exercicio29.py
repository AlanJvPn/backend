from pydantic import BaseModel, ValidationError, Field

pokemons = {}
pokemons_capturados = []

class Pokemon(BaseModel):
    nome_pkm: str
    tipo_pkm: str
    nivel_pkm: int = Field(ge=1, le=100)

def exibir_menu():
    return (
        "\n--- PokéDex ---\n"
        "1. Adicionar Pokémon\n"
        "2. Listar Pokémon\n"
        "3. Remover Pokémon\n"
        "4. Atualizar nível do Pokémon\n"
        "5. Registrar captura de Pokémon\n"
        "6. Exibir histórico de captura\n"
        "7. Sair"
    )

def validar_pokemon(pokedex, nome):
    if nome in pokedex:
        return True
    else:
        print(f"\nErro: O Pokémon '{nome}' não está na PokéDex.")
        return False

def adicionar_pokemon(pokedex):
    print("\n--- Cadastro de Pokémon ---")

    input_nome = input("Digite o nome do Pokémon: ")
    if input_nome in pokedex:
        print(f"O Pokémon '{input_nome}' já existe na Pokédex!")
        return

    input_tipo = input("Digite o tipo do Pokémon: ")
    input_nivel = input("Digite o nível do Pokémon (1 a 100): ")

    try:
        novo_pokemon = Pokemon(
            nome_pkm=input_nome, tipo_pkm=input_tipo, nivel_pkm=input_nivel
        )

        pokedex[novo_pokemon.nome_pkm] = novo_pokemon.model_dump()
        print(f"{novo_pokemon.nome_pkm} adicionado com sucesso!")

    except ValidationError:
        print("\nErro: Valores inválidos. O nível deve ser de 1 a 100.")

def listar_pokemons(pokedex):
    if not pokedex:
        return "\nNão há pokemons registrados."
    else:
        exibir = []
        for nome, dados in sorted(pokedex.items()):
            tipo = dados["tipo_pkm"]
            nivel = dados["nivel_pkm"]
            exibir.append(f"Nome: {nome} | Tipo: {tipo} | Nível: {nivel}")
        return "\n" + "\n".join(exibir)

def remover_pokemon(pokedex, nome):
    if validar_pokemon(pokedex, nome):
        del pokedex[nome]
        return f"Pokémon {nome} libertado com sucesso!"
    return "" 

def atualizar_pokemon(pokedex, nome):
    if validar_pokemon(pokedex, nome):
        novo_nivel = input(f"Digite o novo nível do {nome} (1 a 100): ")

        try:
            dados_atualizados = pokedex[nome].copy()
            dados_atualizados['nivel_pkm'] = novo_nivel
            pokemon_atualizado = Pokemon(**dados_atualizados)

            pokedex[nome] = pokemon_atualizado.model_dump()
            print(f"Nível do {nome} atualizado para {pokemon_atualizado.nivel_pkm} com sucesso!")

        except ValidationError:
            print("\nErro: O nível deve ser um número inteiro entre 1 e 100.")

def registrar_captura(pokedex, capturados, nome, quantidade):
    if validar_pokemon(pokedex, nome):
        try:
            qtd = int(quantidade) 
            
            for entrada in capturados:
                if entrada[0] == nome:
                    entrada[1] += qtd
                    return f"Mais {qtd} captura(s) adicionada(s) ao {nome} com sucesso!"
            
            capturados.append([nome, qtd])
            return f"{qtd} captura(s) registrada(s) para {nome} com sucesso!"
                
        except ValueError:
            return "\n Erro: A quantidade deve ser um número."
            
    return ""

def exibir_historico_capturas(capturados):
    if not capturados:
        return "\nNão há histórico de capturas."
    
    historico = []
    for entrada in capturados:
        nome = entrada[0]
        quantidade = entrada[1]
        historico.append(f"Pokémon: {nome} - Qtd: {quantidade}")
        
    return "\n" + "\n".join(historico)

def menu():
    while True:
        print(exibir_menu())
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_pokemon(pokemons)
        elif escolha == "2":
            print(listar_pokemons(pokemons))
        elif escolha == "3":
            nome = input("Digite o pokémon que vai libertar: ")
            print(remover_pokemon(pokemons, nome))
        elif escolha == "4":
            nome = input("Digite o pokémon: ")
            atualizar_pokemon(pokemons, nome)
        elif escolha == "5":
            nome = input("Digite o pokémon: ")
            quantidade = input("Digite quantas vezes o pokémon foi capturado: ")
            print(registrar_captura(pokemons, pokemons_capturados, nome, quantidade))
        elif escolha == "6":
            print(exibir_historico_capturas(pokemons_capturados))
        elif escolha == "7":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\n Opção inválida!")

if __name__ == "__main__":
    menu()