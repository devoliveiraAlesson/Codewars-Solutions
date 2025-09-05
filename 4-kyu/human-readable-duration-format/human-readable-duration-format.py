def format_duration(seconds):
    ano = seconds//31536000
    dia = (seconds % 31536000) // 86400
    hora = ((seconds % 31536000) % 86400) // 3600
    minuto = (((seconds % 31536000) % 86400) % 3600) // 60
    segundo = (((seconds % 31536000) % 86400) % 3600) % 60
    
    
    if ano > 1:
        ano = f"{ano} years"
    elif ano:
        ano = f"{ano} year"
    
    if dia > 1:
        dia = f"{dia} days"
    elif dia:
        dia = f"{dia} day"
    
    if hora > 1:
        hora = f"{hora} hours"
    elif hora:
        hora = f"{hora} hour"
        
    if minuto > 1:
        minuto = f"{minuto} minutes"
    elif minuto:
        minuto = f"{minuto} minute"
    
    if segundo > 1:
        segundo = f"{segundo} seconds"
    elif segundo:
        segundo = f"{segundo} second"
    else:
        pass
    
    resultado = []
    
    for i in ano, dia, hora, minuto, segundo:
        if i:
            resultado.append(i)
            
    if [ano, dia, hora, minuto] and len(resultado) > 1:
        return ", ".join(resultado[0:len(resultado) - 1]) + " and " + resultado[-1]
    elif len(resultado) > 0:
        return "".join(resultado)
    else:
        return "now"