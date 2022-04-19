# PAWM-Progetto
Progetto sito web 

Relazione Progetto - sito web saloneCla - PAWM 
Questo progetto consiste nella presentazione di un sito web, 
sviluppato con il framework Django ed il linguaggio Python. 

Viene utilizzato Django in quanto molto efficiente e scalabile, 
inoltre permette lo sviluppo tramite il pattern MVC (Model-View-Controller),
che in Django corrisponde a MTV (Model, Template e View) 
che permette di separare le parti del codice dando ad ognuno la propria responsabilità. 

Dove nel Model abbiamo la struttura, i Template corrispondono alle viste; 
quindi, come viene visualizzato il modello e le views che corrisponde al controller,il gestore del tutto. 
Le views in Django sono delle funzioni che prendono una richiesta (request) come, ad esempio, 
l’url e restituiscono una risposta (response), cioè una pagina HTML.

Come database viene utilizzato MySQL Workbench, che utilizza SQL, basato sul modello relazionale DBMS. Tutto ruota attorno il concetto di “tabella” e relazioni tra esse. 

Pe quanto riguarda la parte grafica e quindi i template è stato utilizzato il linguaggio di markup HTML unito ai fogli di stile CSS, ed utilizzata la libreria di Bootstrap.

Per la parte di Login viene utilizzato Firebase e la libreria per Django “pyrebase 4”. 

Nello specifico tale sito web rappresenta un salone di vendita di automobili. 

Infatti, nel modello, viene rappresentato lo scheletro di una generica auto con nome, marca, prezzo, anno, dettagli, 
km e immagine della stessa, 
dove tali categorie corrispondono a colonne della tabella “auto” nel database.
Per fare ciò in Django vengono utilizzate le migrazioni. 

Poi una volta che abbiamo recuperato le auto dal database, 
possiamo mostrarle alla vista, cioè ai template in Django, 
dove abbiamo la pagina che mostra tutte le auto e un campo 
di ricerca per trovare una singola auto ed ottenere i dettagli della stessa. 
Questo progetto è un esempio di sito web, 
integrando un sistema di login esterno,
utilizzando un database per il popolamento dei dati 
e utilizzare il paradigma REST ed i suoi principi: 
come ad esempio l’architettura client-server, inoltre, 
importanti sono le chiamate stateless, 
e quindi fornire le API stateless.
Nel file settings.py troviamo le configurazioni, 
mentre nel file urls.py 
troviamo tutti i percorsi e quindi tutte le rotte della nostra applicazione. 
