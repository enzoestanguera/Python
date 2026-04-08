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