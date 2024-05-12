

# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on sudoku-peli, jossa pelaaja voi syöttää numeroita sudoku-ruudukkoon ja tarkastaa, onko peliruudukko täytetty oikein. Pelejä on eri vaikeusasteissa, ja pelaaja voi valita haluamansa tason. Pelin alussa pelaana syöttää nimensä, ja peli mittaa ruudukon täyttöön käytettävää aikaa ja tallentaa pelaajan pelaamat pelit.

## Käyttöliittymä

Graafisessa käyttöliittymässä on esinäkymä, jossa pelaaja voi syöttää nimensä ja valita ruuduko vaikeustason. Valinnan jälkeen siirrytään varsinaiseen peliruudukkoon. Varsinaisessa pelinäkymässä on joitakin valmiita syötteitä omaava sudoku-ruudukko, johon käyttäjä voi syöttää numeroita. Syötteiden oikeellisuuden voi tarkastaa painamalla tarkastus-nappulaa. Mikäli koko ruudukko on täytetty ja kaikki syötteet ovat oikein, tallentaa tarkastus-nappi ruudukon täyttöön menneen ajan pelaajan tietojen kanssa.


## Toiminnallisuus

- Sovellus esittää esinäkymässä kentän, johon pelaajan nimi syötetään. TEHTY
- Sovellus esittää esinäkymässä painikkeet, josta voi valita pelin vaikeustason. TEHTY
- Pelinäkymässä sovellus esittää osittain täytetyn sudoku-ruudukon pelaajalle. TEHTY
- Pelaaja voi syöttää ruudukon soluihin numeroita TEHTY
- Pelaaja voi poistaa syöttämänsä numeron. TEHTY
- Pelaaja ei voi poistaa ruudukossa valmiina ollutta numeroa. TEHTY
- Käyttöliittymässä on tarkasta-toiminto, jonka avulla syötteiden oikeellisuuden voi tarkastaa TEHTY
  - Sovellus tarkastaa rivien oikeellisuuden TEHTY
  - Sovellus tarkastaa sarakkeiden oikeellisuuden TEHTY
  - Sovellus tarkastaa ruutujen oikeellisuuden TEHTY
  - Mikäli kaikki ruudut on täytetty oikein, sovellus tarkastaa onko ruudukko valmis. TEHTY
  - Väärin täytettyjen ruutujen, sarakkaiden tai rivien koordinaatit ilmoitetaan pelaajalle tarkastus-nappulaa painettaessa TEHTY
- Uuden ruudukon pohja haetaan tietokannasta TEHTY
- Sovellus tallentaa pelaajan ruudukon täyttämiseen käytetyn ajan, ja tallentaa sen tietokantaan pelaajan tietojen kanssa.

