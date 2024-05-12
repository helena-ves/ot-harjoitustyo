# Ohjelmistotekniikka, harjoitustyö

Tämä on  ohjelmistotekniikka-kurssin  harjoitustyönä tehty sudoku-sovellus. On suositeltavaa, että sovellusta käytettäessä pythonista on käytössä vähintään versio 3.8 ja mieluiten 3.10.

## Ohjelman suorittaminen

Ohjelman voi asentaa seuraavasti:
```
poetry install
```
Asennuksen jälkeen:
```
poetry run invoke build
```
Ja lopuksi sovelluksen voi käynnistää komennolla
```
poetry run invoke start
```
## Ohjelman käyttöohjeet

Kun ohjelma on käynnistetty (ks. ohje ylempänä), aloitusnäyttö avautuu. Pelaaja syöttää valitsemansa nimen, tunnuksen tai lempinimen sille varatulle kentälle.
Kenttä aktivoituu klikkaamalla. Nimen syöttämisen jälkeen valitaan pelin vaikeustaso napeista "Easy", "Medium" tai "Hard". Vaikeustason valinnan jälkeen peli
lataa pelaajalle joitakin valmiita numeroita sisältävän sudoku-ruudukon.

Kun peliruudukko on näkyvillä, voi ruutuihin syöttää minkä tahansa numeron. Ruudut aktivoituvat klikkaamalla. Oman syötteen voi perua aktivoimalla ruudun ja painamalla välilyönti-näppäintä.
Tällöin ruutu tyhjenee. Omien syötteiden oikeellisuuden voi tarkastaa painamalla nappia "Check progress". Mikäli sovellus löytää virheitä, niiden koordinaatit ilmoitetaan käyttäjälle ruudukon alapuolella.
Koordinaattien nollapiste on vasemmassa yläkulmassa, ja rivit ovat numeroitu nollasta kahdeksaan, ylhäältä alas. Sarakkeet on numeroitu vasemmalta oikealle ja nollasta kahdeksaan. Ruutujen koordinaatit ilmoitetaan ko. ruudun vasemman yläkulman koordinaattien avulla siten, että ylimmän rivin ruutujen koordinaatit vasemmalta oikealle ovat (0, 0), (0, 3), ja (0, 6).

Mikäli ruudukko on täytetty oikein, ilmoittaa sovellus nappia painamalla kaikkien syötteiden olevan oikein. Kun ruudukko on täytetty kokonaan oikein, "Check progress" nappula ilmoittaa pelin olevan valmis.
Tämän jälkeen pelaajan täyttämä nimi, ruudukon vaikeustaso ja ruudukon täyttöaika tallennetaan tietokantaan.

### Sudokun säännöt

Sudoku-ruudukko tulee täyttää siten, että jokaisella rivillä ja sarakkeella sekä jokaisessa ruudussa toistuvat numerot yhdestä yhdeksään. Jokainen numero saa
esiintyä rivillä, sarakkeella ja ruudulla vain kerran. Esimerkiksi kaksi numero kahdeksaa samalla rivillä sisältävä ruudukko on virheellisesti täytetty. Peli
päättyy, kun jokainen ruudukon ruutu on täytetty oikein.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/helena-ves/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/helena-ves/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Työaikakirjanpito](https://github.com/helena-ves/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/helena-ves/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Ohjelman testaus ja testikattavuus

Ohjelman sisältämät testit voi suorittaa komennolla:
```
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla:
```
poetry run invoke coverage-report
```

## Release

[Release](https://github.com/helena-ves/ot-harjoitustyo/releases)
