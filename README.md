# Z-ROOM Check-In System

Dette projekt er et simpelt check-in system til Z-ROOM, hvor brugere kan checke ind via en pinkode, der valideres mod en SQL Server database. Systemet består af en Flask webserver, en CO2/temperaturmåler og et simpelt webinterface.

## Funktioner

- Webinterface til check-in og pinkodeindtastning
- Pinkodevalidering mod SQL Server database
- CO2 og temperaturmåling med LED-indikator (separate script)
- Responsivt design og brugervenlig feedback

## Projektstruktur

```
co2-temp.py           # Script til CO2/temperaturmåling og LED-styring
server.py             # Flask webserver med pinkodevalidering
static/
    pin.js            # JavaScript til pinkodevalidering på klientsiden
    style.css         # CSS-styling
templates/
    index.html        # Forside med check-in knap
    indtastpin.html   # Pinkodeindtastningsside
```

## Installation

1. **Krav**  
   - Python 3.x  
   - Flask  
   - flask_cors  
   - pyodbc  
   - GPIO Zero (kun til Raspberry Pi og co2-temp.py)  
   - scd30_i2c (til CO2-sensor)

2. **Installer afhængigheder**
   ```sh
   pip install flask flask_cors pyodbc gpiozero
   ```

3. **Opsæt ODBC Driver**  
   Installer ODBC Driver 18 for SQL Server på din Raspberry Pi/server.

## Kørsel

### Flask Webserver

```sh
python server.py
```

### CO2/Temperaturmåling

```sh
python co2-temp.py
```

## Brug

1. Åbn webinterfacet i din browser.
2. Klik på "Check In" og indtast din pinkode.
3. Systemet validerer pinkoden og giver adgang hvis den er gyldig.

## Sikkerhed

- Pinkoder sendes kun via POST og valideres på serveren.
- Databaseoplysninger bør holdes sikre og evt. flyttes til miljøvariabler i produktion.

## Licens

Dette projekt er kun til undervisningsbrug.

---

*Udviklet af Ø'erne.*
