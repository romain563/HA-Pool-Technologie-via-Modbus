
MODELS = {
    "ibasel_duo": {
        "name": "Ibiza iBasel Duo",
        "sensors": [
            {
                "name": "Taille du bassin",
                "translation_key": "taille_bassin",
                "unique_id": "taille_bassin",
                "address": 4111,
                "unit": "m³",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:texture-box"
            },
            {
                "name": "pH",
                "translation_key": "pH",
                "unique_id": "pH",
                "address": 259,
                "scale": 0.001,
                "precision": 1,
                "icon": "mdi:test-tube"
            },
            {
                "name": "Température de l'eau",
                "translation_key": "temperature_eau",
                "unique_id": "temperature_eau",
                "address": 260,
                "unit": "°C",
                "scale": 0.1,
                "precision": 1,
                "icon": "mdi:thermometer-water",
                "device_class": "temperature"
            },
            {
                "name": "Salinité",
                "translation_key": "taux_sel",
                "unique_id": "taux_sel",
                "address": 261,
                "unit": "g/L",
                "scale": 0.1,
                "precision": 1,
                "icon": "mdi:shaker-outline"
            },
            {
                "name": "ORP",
                "translation_key": "orp",
                "unique_id": "orp",
                "address": 262,
                "unit": "mV",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:lightning-bolt"
            },
            {
                "name": "Consigne pH",
                "translation_key": "consigne_ph",
                "unique_id": "consigne_ph",
                "address": 4207,
                "scale": 0.000390625,
                "precision": 1,
                "icon": "mdi:cog"
            },
            {
                "name": "Consigne ORP",
                "translation_key": "consigne_orp",
                "unique_id": "consigne_orp",
                "address": 4235,
                "unit": "mV",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:cog"
            }
        ]
    },
    "poolsquad_uv": {
        "name": "Poolsquad UV",
        "sensors": [
            {
                "name": "Taille du bassin",
                "translation_key": "taille_bassin",
                "unique_id": "taille_bassin",
                "address": 4111,
                "unit": "m³",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:texture-box"
            },
            {
                "name": "pH",
                "translation_key": "ph",
                "unique_id": "ph",
                "address": 259,
                "unit": "pH",
                "scale": 0.001,
                "precision": 2,
                "icon": "mdi:test-tube"
            },
            {
                "name": "Température de l'eau",
                "translation_key": "temperature_eau",
                "unique_id": "temperature_eau",                
                "address": 260,
                "unit": "°C",
                "scale": 0.1,
                "precision": 1,
                "icon": "mdi:thermometer-water",
                "device_class": "temperature"
            },
            {
                "name": "Taux de sel",
                "translation_key": "taux_sel",
                "unique_id": "taux_sel",
                "address": 261,
                "unit": "g/L",
                "scale": 0.1,
                "precision": 1,
                "icon": "mdi:shaker-outline"
            },
            {
                "name": "ORP",
                "translation_key": "orp",
                "unique_id": "orp",
                "address": 262,
                "unit": "mV",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:lightning-bolt"
            },
            {
                "name": "Total injection pH",
                "translation_key": "total_injection_ph",
                "unique_id": "total_injection_ph",
                "address": 4213,
                "unit": "minutes",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:test-tube"
            },            
            {
                "name": "Consigne pH",
                "translation_key": "consigne_ph",
                "unique_id": "consigne_ph",
                "address": 4207,
                "unit": "pH",
                "scale": 0.000390625,
                "precision": 1,
                "icon": "mdi:cog"
            },
            {
                "name": "Consigne ORP",
                "translation_key": "consigne_orp",
                "unique_id": "consigne_orp",
                "address": 4235,
                "unit": "mV",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:cog"
            },
            {
                "name": "Consigne Electrolyse",
                "translation_key": "consigne_electrolyse",
                "unique_id": "consigne_electrolyse",
                "address": 4168,
                "unit": "%",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:cog"
            },
            {
                "name": "Fonctionnement Electrolyse",
                "translation_key": "fonctionnement_electrolyse",
                "unique_id": "fonctionnement_electrolyse",
                "address": 770,
                "unit": "%",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:cog"
            }
        ]
    },
    "Waterair_gold": {
        "name": "Waterair Gold",
        "sensors": [
            {
                "name": "Taille du bassin",
                "translation_key": "taille_bassin",
                "unique_id": "taille_bassin",
                "address": 4111,
                "unit": "m³",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:car-coolant-level",
                "device_class": "volume"
            },
            {
                "name": "pH",
                "translation_key": "pH",
                "unique_id": "pH",
                "address": 259,
                "scale": 0.001,
                "precision": 2,
                "icon": "mdi:ph",
                "device_class": "ph"
            },
            {
                "name": "Température de l'eau",
                "translation_key": "temperature_eau",
                "unique_id": "temperature_eau",                
                "address": 260,
                "unit": "°C",
                "scale": 0.1,
                "precision": 1,
                "icon": "mdi:thermometer-water",
                "device_class": "temperature"
            },
            {
                "name": "Salinité",
                "translation_key": "taux_sel",
                "unique_id": "taux_sel",
                "address": 261,
                "unit": "g/L",
                "scale": 0.1,
                "precision": 1,
                "icon": "mdi:shaker-outline"
            },
            {
                "name": "ORP",
                "translation_key": "orp",
                "unique_id": "orp",
                "address": 262,
                "unit": "mV",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:lightning-bolt"
            },
        #    {
        #        "name": "Total injection pH",
        #        "translation_key": "total_injection_ph",
        #        "unique_id": "total_injection_ph",
        #        "address": 4213,
        #        "unit": "minutes",
        #        "scale": 1,
        #        "precision": 0,
        #        "icon": "mdi:test-tube"
        #    },            
            {
                "name": "Consigne pH",
                "translation_key": "consigne_ph",
                "unique_id": "consigne_ph",
                "address": 4207,
                "scale": 0.000390625,
                "precision": 1,
                "icon": "mdi:ph",
                "device_class": "ph"
            },
            {
                "name": "Consigne ORP",
                "translation_key": "consigne_orp",
                "unique_id": "consigne_orp",
                "address": 4235,
                "unit": "mV",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:cog"
            },
#            {
#                "name": "Consigne électrolyse",
#                "translation_key": "consigne_electrolyse",
#                "unique_id": "consigne_electrolyse",
#                "address": 4168,
#                "unit": "%",
#                "scale": 1,
#                "precision": 0,
#                "icon": "mdi:cog"
#            },
            {
                "name": "Puissance électrolyse",
                "translation_key": "fonctionnement_electrolyse",
                "unique_id": "fonctionnement_electrolyse",
                "address": 770,
                "unit": "%",
                "scale": 1,
                "precision": 0,
                "icon": "mdi:flash-outline"
            },
            {
                "name": "Concentration correcteur de pH",
                "translation_key": "concentration_correcteur_ph",
                "unique_id": "concentration_correcteur_ph",
                "address": 4208,
                "unit": "%",
                "scale": 1 ,
                "precision": 1,
                "icon": "mdi:code-brackets",
                "device_class": "ph"
            },
            {
                "name": "Mode électrolyse",
                "translation_key": "mode_electrolyse",
                "unique_id": "mode_electrolyse",
                "address": 4171
            }
            #Régulation pH auto=1, off=0
#            {
#                "name": "Régulation pH",
#                "translation_key": "regulation_pH",
#                "unique_id": "regulation_pH",
#                "address": 4200
#            }
        ]
    }
}


