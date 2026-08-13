
opcao = ""

while opcao != "5":

  print("=== Calculadora ===")
  print("1 - Adição: ")
  print("2 - Subtração: ")
  print("3 - Multiplicação: ")
  print("4 - Divisão: ")
  print("5 - Sair.")

  opcao = input("Selecione uma operação: ")

  if opcao == "5":
    print("Calculadora encerrada.")
    break

  if opcao in ["1", "2", "3", "4"]:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if opcao == "1":
      resultado = num1 + num2
      print("O resultado é: ", resultado)

    elif opcao == "2":
      resultado = num1 - num2
      print("O resultado é: ", resultado)

    elif opcao == "3":
       resultado = num1 * num2
       print("O resultado é: ", resultado)

    elif opcao == "4":
       resultado = num1 / num2
       print("O resultado é: ", resultado)

  else:
    print("Por favor, tente novamente")

