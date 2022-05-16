def produtoMenorCinco(resultado):
 #Recebe uma lista do tipo[('produto',quantidade), (),()]
 # Retorna (produto)
 total =0
 for elemento in resultado:
  if (elemento[1] < 5):
    total +=1
  return total
