#exemplo com numero (int)
n = int (input("numero 1: "))

match n:
    case 1:
        print(f'valor 1{n}')
    case 2:
        print(f'n valor 2 {n}')
    case 3:
        print(f'n valor 3 {n}')
    case __:
        print(f'numero invalido')

    #exemplo com texto (str)

status = (input('Status:'))

match status :
            case'Pedente' | 'pendente' | 'PENDENTE':
                print('aguaradando pagamento')
            case'Pago' | 'pago' | 'PAGO':
             print('preparando para envio')
            case 'Enviado' | 'enviado' | 'ENVIADO ':
               print('Produto a caminho')
            case 'Entregue' | 'entregue' 'ENTREGUE':
               print('pedido finalizado')
            case _:
               print(f'status {status} não reconhecido!')