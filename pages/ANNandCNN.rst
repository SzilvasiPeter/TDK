Neurális hálózatok általános bevezető 

A neurális hálózattokat gyakran hasonlítjuk az emberi agy működéséhez. Ha körültekintően szemügyre vesszük agyunk működését, akkor azt tapasztaljuk, hogy neuronokból és közöttük felépülő kapcsolatokból áll össze. A külvilágból érkezett ingereket értelmezhetjük úgy, mint egy bemenetet, amit az agyunkban lévő neuronok feldolgoznak. 

 

A kutatók az agy felépítését vizsgálva egy olyan matematikai modellt dolgoztak ki, amely   reprezentálni próbálja az agyban található neuronokat és a közöttük lévő kapcsolatokat. Ezt a modellt nevezzük neurális hálónak vagy neurális hálózatnak.  

A neurális hálózatot alkotó neuronok úgynevezett rétegekbe rendeződnek. Háromféle réteget különbözetünk meg, a bemeneti, a kimeneti és a rejtett réteget. Bemeneti és kimeneti rétegből minden hálózatban egy darab van, rejtett rétegből azonban tetszőleges számú lehet. 

A hálózatban a rétegeket élek kötik össze egymással, amelyekhez egyenként egy-egy súly tartozik. A neuronok a bemeneti éleiken kapott értékek és a súlyok segítségével bizonyos műveleteket végeznek el, majd az eredmény a kimeneti éleiken keresztül továbbítják a következő réteg neuronjai felé. 

A tanítási folyamat elvégzésekor a hálózatba olyan bemenetet juttatunk, amelyhez tartozó kimenet ismert. A bemenetet végig futtatjuk a hálózat rétegein, majd a kimeneti réteg által szolgáltatott eredményt összehasonlítjuk a kimenet várt értékével. A kér érték közötti eltérést a hálózat hibájának nevezzük. A tanítás folyamán a hálózat súlyait úgy változtatjuk, hogy ez a hiba lehetőleg minél kisebb legyen. A hálózat betanítása után már olyan bemeneteket is megadhatunk, amelyeknek már nem ismerjük a kimenetét, és a hálózat ezekre is képes hibahatáron belüli kimenetet produkálni. 

 

Perceptron 

Az egyszerűség kedvéért vizsgáljunk meg egy olyan neurális hálózatot, amelynek egyetlen neuronnal rendelkezik. Ezt szokás Perceptron-nak is nevezni. 

Részei: 

Bemenet: Az kiértékelendő adat (ember számára ingerek), amit általában egy vektor (x) reprezentál. 

Súlyok: Két neuron közötti kapcsolat. Egy valós szám (eleinte véletlenszerűek). A hálózat súlyait (W) mátrixba tároljuk el.  

Összegző csomópont: A bemeneteket összeszorozza a megfelelő súlyokkal és ezek összegét képezi. Tulajdonképpen mátrix szorzásról van szó. KÉPLET:  

v(n) = Σ_i^{n}(w_i*x_i) 

Aktivációs függvény: Egy olyan függvény (φ), ami leképezi a kapott összeget egy kisebb intervallumba pl. [0,1] vagy [-1,1] között. 

Kimenet: A leképezett értékünk lesz a kimenetünk (y). 

 

A képen láthatunk egy b_n változot másnéven bias, amitől eltekinthetünk. NOTE: Mi történe ha az összes súly 0 értékű? (nem aktiválódik a neuron -> probléma) 

Backpropagation 

Amennyiben az x(n) bemenethez tartozó ideális kimenetet d(n)-nel jelöljük, illetve y(n) jelenti a hálózat által az x(n) bemenetre adott kimenetét, a neurális hálózat négyzetes hibáját a következőképpen értelmezzük: Képlet!! ε = (d ( n ) − y ( n ))^2 

Ezt a hibát akarjuk a tanítási eljárás során minimálisra csökkenteni. Természetesen az lenne az ideális, ha a hibát egészen nullára tudnánk redukálni, de ez általában nem sikerül, ezért meg kell elégednünk egy kellően kicsiny hibaküszöbbel. 

GRADIENS DECENT-el kiegészíteni 3BLUE1BROWN!!! Képek magyarázat

Konvolúciós neurális hálózat 

Ahhoz, hogy a célkitűzésünket, az optikai karakterfelismerést meg tudjuk valósítani, közelebbről is meg kell vizsgálnunk a karakterfelismerő rendszerekben alapelemként   használatos neurális hálózattokat és azok működését.   Akármilyen jó és bonyolult modellt alkottak is a tudósok, a neurális hálózat mégsem lett   alkalmas az agy gondolkodásának rekonstruálására, csupán a tanulás képességét „örökölte”.   Amennyiben azonban kellően nagy tanítási adatbázissal rendelkezünk, a betanított hálózat olyan adatokról is képes információkat adni, amelyekkel korábban még nem találkozott.  