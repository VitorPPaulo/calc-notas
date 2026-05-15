nota_min = 0.0
nota_max = 10.0
media_aprovacao = 7.0
media_reprovacao = 4.0
def valida(nota):
    if not(nota_min<=nota<=nota_max):
        raise ValueError(f"Nota fora do intervalo: {nota}")
def calcula_media(n1, n2, n3):
    for n in (n1,n2,n3):
        valida(n)
    return(n1+n2+2*n3)/4
def situacao(media):
    if media >= media_aprovacao:
        return "aprovado"
    if media >= media_reprovacao:
        return "recuperacao"
    return "reprovado"
