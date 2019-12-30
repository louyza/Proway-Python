terminal = ['piloto', 'oficial1', 'oficial2', 'chefe', 'comissaria1', 'comissaria2', 'presidiário', 'policial']
aviao = []



def ida(p1, p2):
  print(f'estão no terminal: {terminal}.\n')
  terminal.remove(p1)
  terminal.remove(p2)
  print(f'{p1} está dirigindo o carrinho e {p2} é o passageiro, estão a caminho do avião.\n')
  aviao.append(p1)
  aviao.append(p2)
    
def volta(p1):
  print(f'estão no avião {aviao}\n')
  aviao.remove(p1)
  print(f'{p1} está dirigindo o carrinho a caminho do terminal\n')
  terminal.append(p1)
  print(f'{p1} chegou ao terminal\n')                                                                                            
