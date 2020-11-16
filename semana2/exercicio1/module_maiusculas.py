def maiusculas ( frase ):
    capitalizadas = [ f for f in frase if f.isupper() ]
    return "".join( capitalizadas )
