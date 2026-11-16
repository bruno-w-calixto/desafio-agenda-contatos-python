lista_contatos = []

# 1
def adicionar_contato(nome, telefone, email, favorito):
  contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    "favorito": favorito
  }
  lista_contatos.append(contato)

# 2
def mostrar_lista(lista_contatos):
  for contato in lista_contatos:
    print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {contato['favorito']}")

# 3
def alterar_contato(lista_contatos):
  nome_procurado = input("Qual contato deseja alterar? ")

  for contato in lista_contatos:
    if contato["nome"] == nome_procurado:

      print("\nO que deseja alterar?")
      print("1. Nome")
      print("2. Telefone")
      print("3. Email")
      print("4. Favorito")

      escolha = input("Digite sua escolha: ")

      if escolha == "1":
        novo_nome = input("Digite o novo nome: ")
        contato["nome"] = novo_nome

      elif escolha == "2":
        novo_telefone = input("Digite o novo telefone: ")
        contato["telefone"] = novo_telefone

      elif escolha == "3":
        novo_email = input("Digite o novo email: ")
        contato["email"] = novo_email

      elif escolha == "4":
        novo_favorito = input("Digite o novo favorito (s/n): ")

        if novo_favorito.lower() == "s":
          contato["favorito"] = True
        elif novo_favorito.lower() == "n":
          contato["favorito"] = False
        else:
          print("Opção inválida.")
          return

      else:
        print("Opção inválida.")
        return

      print("Contato atualizado com sucesso!")
      return

  print("Contato nao encontrado.")

# 4
def mudar_favorito(lista_contatos):
  nome_procurado = input("Qual contato deseja marcar/desmarcar como favorito? ")
  for contato in lista_contatos:
    if contato["nome"] == nome_procurado:

      resposta = input("Deseja marcar como favorito? (s/n): ")

      if resposta.lower() == "s":
        contato["favorito"] = True

      elif resposta.lower() == "n":
        contato["favorito"] = False

      else:
        print("Opção inválida.")
        return

      print("Contato atualizado com sucesso!")
      return
    
  print("Contato não encontrado.")

# 5
def mostrar_favoritos(lista_contatos):
  print("\nLista de Contatos Favoritos:")
  for contato in lista_contatos:
    if contato["favorito"]:
      print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

# 6
def apagar_contato(lista_contatos):
  nome_procurado = input("Qual contato deseja apagar? ")

  for contato in lista_contatos:
    if contato["nome"] == nome_procurado:
      lista_contatos.remove(contato)
      print("Contato apagado com sucesso!")
      return
  print("Contato nao encontrado.")


while True:
  print("\nAgenda de Contatos")
  print("1. Adicionar contato")
  print("2. Mostrar lista de contatos")
  print("3. Alterar contato")
  print("4. Mudar favorito")
  print("5. Mostrar favorito")
  print("6. Apagar contato")
  print("7. sair")

  escolha = input("Digite sua escolha: ")

  if escolha == "1":
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    adicionar_contato(nome, telefone, email, False)

  elif escolha == "2":
    mostrar_lista(lista_contatos)

  elif escolha == "3":
    alterar_contato(lista_contatos)

  elif escolha == "4":
    mudar_favorito(lista_contatos)

  elif escolha == "5":
    mostrar_favoritos(lista_contatos)

  elif escolha == "6":
    apagar_contato(lista_contatos)

  elif escolha == "7":
    break

  else:
    print("Opção inválida! Tente novamente.")

print("Agenda encerrada!")


