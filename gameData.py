quiz = {
    1: {
        "pregunta": "¿Cuantos tipos de aminoácidos conforman las proteínas?",
        "contexto" : """Los aminoacidos son anfolitos (reaccionan tanto con los ácidos como con las bases).
Cuentan con un grupo amino (NH2) y un grupo Carboxilico (COOH) y siempre hay un átomo de carbono entre estos grupos.
También cuentan con un tercer grupo variable denominado 'R' el cual termina de definir la naturaleza del aminoacido""",
        "opciones": {
            "1": ["64 aminoacidos", False],
            "2": ["22 aminoacidos", True],
            "3": ["4 aminoacidos", False],
            "4": ["19 aminoacidos", False],
        },
    },
    2: {
        "pregunta": "¿Que es la transcripción?",
        "contexto" : """El ARN, al igual que el ADN son Acidos nucleicos. Estos constituyen el material genetico de los organismos y son necesarios para el
almacenamiento y la excreción de la informacion genetica""",
        "opciones": {
            "1": ["Es el proceso en el que el ARNm copia un gen concreto", True],
            "2": ["Es el proceso en el que los codones se traducen a aminoacidos", False],
            "3": ["Es cuando el ARNm sale del nucleo", False],
            "4": ["Es el proceso en el que se crean las proteinas", False],
        },
    },
    3: {
        "pregunta": "¿Donde ocurre la transcripción?",
        "opciones": {
            "1": ["Es el citoplsma", False],
            "2": ["En el ribosoma", False],
            "3": ["En el nucleo", True],
            "4": ["En la enzima 'ARN polimerasa'", False],
        },
    },
    4: {
        "pregunta": "Que es la traduccion",
        "opciones": {
            "1": ["Es el proseso en el cual el ARNm hace una copia de un gen", False],
            "2": ["Es el proceso en el cual se lee el ARNm para generar cadenas de aminoacidos", True],
            "3": ["Es el proceso en el cual la enzima 'ARN polimerasa' crea al ARNm", False],
            "4": ["Es cuando la cadena de aminoacidos se dobla para formar una estructura 3D compleja y asi crear la proteina", False],
        },
    },
    5: {
        "pregunta": "¿Donde ocurre la traduccion?",
        "opciones": {
            "1": ["Es el citoplsma", True],
            "2": ["En el ADN", False],
            "3": ["En el nucleo", False],
            "4": ["En la enzima 'ARN polimerasa'", False],
        },
    },
    6: {
        "pregunta": "¿A quien se la concidera la madre de la bioinformatica?",
        "contexto" : """(11 de marzo de 1925 - 5 de febrero de 1983) fue una fisicoquímica estadounidense y pionera en el campo de la bioinformática
Dedicó su carrera a aplicar las tecnologías computacionales en evolución para respaldar los avances en biología y medicina, más notablemente la
creación de bases de datos de proteínas y ácidos nucleicos y herramientas para interrogar las bases de datos.""",
        "opciones": {
            "1": ["Françoise Barré-Sinoussi", False],
            "2": ["Christine Anne Orengo", False],
            "3": ["Margaret Oakley Dayhoff", True],
            "4": ["Dina Zielinski", False],
        },
    },
}

codones = {
    1 : ["GAG", "Glu", "E"],
    2 : ["AUG", "Met", "M"],
    3 : ["CCU", "Pro", "P"],
    4 : ["UGG", "Trp", "W"],
    5 : ["GAC", "Asp", "D"],
    6 : ["UCU", "Ser", "S"],
    7 : ["UAC", "Tyr", "Y"],
    8 : ["GUG", "Val", "V"],
    9 : ["GCA", "Ala", "A"],
    10 : ["CCC", "Pro", "P"],
}

camino = {
    "1": {
        "pregunta": "La exprecion genica comienza en ____",
        "opciones": {
            "1": ["El citoplasma", False],
            "2": ["El nucleo", True],
            "3": ["El la enizima ARNp", False],
            "4": ["El ribosoma", False],
        },
    },
    "2": {
        "pregunta": "donde al ADN se le une ____",
        "opciones": {
            "1": ["Una enzima 'ARN polimerasa' (ARNp)", True],
            "2": ["Un ARN mensajero (ARNm)", False],
            "3": ["Un grupo bariado de codones", False],
            "4": ["Un acidonucleico", False],
        },
    },
    "3": {
        "pregunta": "para asi crear al ____, que es una copia de un gen espesifico,",
        "opciones": {
            "1": ["aminoacido", False],
            "2": ["codon", False],
            "3": ["ARNm", True],
            "4": ["ARNp", False],
        },
    },
    "4": {
        "pregunta": "a ese proseso se lo llama ____",
        "opciones": {
            "1": ["traducción", False],
            "2": ["transcripción", True],
            "3": ["mutación", False],
            "4": ["plegamiento", False],
        },
    },
    "5": {
        "pregunta": "luego el ARNm sale del nucleo para dirigirse al ____",
        "opciones": {
            "1": ["citoplsma", True],
            "2": ["lisosoma", False],
            "3": ["nucleolo", False],
            "4": ["cromoplasto", False],
        },
    },
    "6": {
        "pregunta": "donde se lee el ARNm para crear ____",
        "opciones": {
            "1": ["codones", False],
            "2": ["proteinas", False],
            "3": ["aminoácidos", True],
            "4": ["celulas", False],
        },
    },
    "7": {
        "pregunta": "una vez creado el ultimo aminoacido la cadena se dobla en una forma 3D para ____",
        "opciones": {
            "1": ["formar la proteina", True],
            "2": ["ocupar menos espacio", False],
            "3": ["viajar mas rapido hacia el nucleo", False],
            "4": ["para fijar los aminoácidos", False],
        },
    },
}
