import folium

# Initial location
the_map = folium.Map(location=[-15.790707, -47.892676], zoom_start=12)

# Parque Deck Sul
# _________________________________________________________________________
# _________________________________________________________________________

folium.Marker(
    location=[-15.837292342147903, -47.90125878707489],
    popup="""
    <div style="
        font-family: Arial, sans-serif;
        color: black;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        width: 200px;
    ">
        <h3 style="color: #2c7efc;">Parque Deck Sul</h3>
        <h5 style="color: #2c7efc;">(Parque dos Pioneiros Cláudio Sant'Anna)</h5>
        <p><b>Pássaros:</b></p>
        <ul>
            <li>Curicaca</li>
            <li>Sabiá-laranjeira</li>
            <li>João-de-barro</li>
            <li>Choca-barrada</li>
            <li>Carão</li>
            <li>Ferreirinho-relógio</li>
            <li>Sanhaço-cinzento</li>
            <li>Curutié</li>
        </ul>
    </div>
    """
    ).add_to(the_map)

# Praça dos Cristais
# _________________________________________________________________________
# _________________________________________________________________________

folium.Marker(
    location=[-15.773107801965622, -47.9210683653937],
    popup="""
    <div style="
        font-family: Arial, sans-serif;
        color: black;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        width: 200px;
    ">
        <h3 style="color: #2c7efc;">Praça dos Cristais</h3>
        <p><b>Pássaros:</b></p>
        <ul>
            <li>Andorinhão-do-buriti</li>
            <li>Tesourinha</li>
            <li>Sabiá-laranjeira</li>
            <li>João-de-barro</li>
            <li>Tucano</li>
        </ul>
    </div>
    """
    ).add_to(the_map)

# Parque Vivencial do Lago Norte
# _________________________________________________________________________
# _________________________________________________________________________

folium.Marker(
    location=[-15.728447499079948, -47.892436752755486],
    popup="""
    <div style="
        font-family: Arial, sans-serif;
        color: black;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        width: 200px;
    ">
        <h3 style="color: #2c7efc;">Parque Vivencial do Lago Norte</h3>
        <p><b>Pássaros:</b></p>
        <ul>
            <li>João-de-barro</li>
            <li>Bem-te-vi</li>
            <li>Sabiá-laranjeira</li>
            <li>Quero-quero</li>
            <li>Choca-barrada</li>
            <li>Suiriri</li>
            <li>Neinei</li>
            <li>Pula-pula</li>
            <li>Fim-fim</li>
            <li>Garibaldi</li>
            <li>Periquito-de-encontro-amarelo</li>
            <li>Canário-da-terra</li>
            <li>Tico-tico</li>
            <li>Juriti-pupu</li>
        </ul>
    </div>
    """
    ).add_to(the_map)


the_map.save("birds_and_plants.html")
