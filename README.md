# TDK

Kínai karakterek felismerése generált minták alapján

* konvolúciós neurális hálók
* domain randomization
* optikai karakterfelismerés
* osztályozás

## Bevezetés

* Domain generálás, ANN előnyei

## Kínai karakterek felismerési módjai

* Karakterkészlettel kapcsolatban írni néhány, felismerés szempontjából fontos jellemzőt!
* Az elérhető OCR-eket összeszedni!
* Vonalvastagsággal, írásmóddal kapcsolatos tudnivalók. (Itt még nem informatikai szempontból, csak úgy általában az írással kapcsolatban.)

## Karakterek reprezentálása és mintagenerálás

### SVG-k feldolgozása

* Az elérhető SVG-s minták feldolgozása. Lehetőleg egy minél egyszerűbb modell kellene, hogy legyen belőle.
* Modell: (x1, y1, t1) - (x2, y2, t2) - ... - (xN, yN, tN)
* Kirajzoló programot összerakni!
* Egymás mellé rakni az eredeti SVG-s és a írásmodell szerinti változatokat.

### Domain randomization

* Domain randomization
* Zajtípusok definiálása. Úgy érdemes megfogalmazni, hogy az invariánciára vonatkozó tartományok megadása például.
* Pontszerű zajok, elmosódások, takarás, vágás, forgatás, gyűrődés (textúrázás), alacsony kontraszt, gradiens.
* Felbontástól való függőség
* Invarianciánként lehet akár más a topológia, tanítási módszer is. (Majdhogynem külön problémaként kezelhető onnastól kezdve.)

## Konvolúciós neurális hálók alkalmazása

* Az osztályozási probléma formális felírása
* Javasolt topológiák áttekintése
* Topológiára vonatkozó javaslatok

## Generálási és tanítási paraméterek hangolása

* Az osztályozási probléma hatékonyságának javítása

## Validáció, további kutatási lehetőségek

* Más nyelvek, más módszerek, további zajok
* Több karakter egyidejű vizsgálata
* További implementáció
* Pontosság javítása
* Rule extraction a kapott hálókra nézve
* Teljesítmény javítása

## Összegzés

* 1-2 oldalban összefoglalni a dolgozat eredményeit!

## Hivatkozások

* Kínai karakterek fő jellemzőivel kapcsolatos irodalom
* Elérhető OCR (jellegű) megoldások
* Konvolúciós neurális hálók
* Domain randomization (főként aktuális cikkek a témakörben)

