# What Polish internet users say and ask about AI

Corpus: **6029** AI-relevant Polish texts, of which **3477** (58%) fall into **30** clusters; the rest is HDBSCAN noise (too idiosyncratic to group).

## 1. Ranked themes

Ranked by size. **Eng. rank** = rank when each text counts `1 + ln(1 + likes)`. **1 video** = share of the cluster coming from its single biggest source video/thread (high → one piece of content may be driving the theme). **Coh.** = model-judged coherence 1–5.

| # | Theme (EN / PL) | Type | Topic | Size | % corpus | Eng. rank | Top source | 1 video | Coh. | Example quote |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AI job loss enriches corporations, impoverishes workers**<br>AI zabiera pracę, zyskują korporacje i elity | fear | jobs_economy | 521 | 8.6% | 1 | youtube=521 | 13% | 3 | „U mnie w firmie lekko polowa ludzi została wywalona. Niby koszty, rezim budzetowy itp ale wiadomo, AI zmienilo to jak sie pracuje. Czesc ludzi niepotrzebna, a …” |
| 2 | **Mass unemployment: who will buy anything?**<br>Masowe bezrobocie: kto kupi, gdy nikt nie zarabia? | fear | jobs_economy | 448 | 7.4% | 2 | youtube=448 | 16% | 4 | „Już teraz tak jest. Pracownicy są zwalniani, zespoły redukowane. Tylko kto kupi produkty firm jeśli nikt nie będzie miał pieniędzy?” |
| 3 | **Scattered sarcastic quips about AI**<br>Sarkastyczne, rozproszone komentarze o AI | joke_cynicism | ai_safety_xrisk | 447 | 7.4% | 3 | youtube=447 | 14% | 1 | „Hodują ai? Teraz to juz ona nas hoduje” |
| 4 | **AI is just a tool that makes mistakes**<br>AI to tylko narzędzie – popełnia błędy | argument_for | capabilities_hype | 336 | 5.6% | 4 | youtube=336 | 13% | 2 | „I jeśli mógłbym udzielić jakiejś wskazówki, dotyczącej AI: traktujcie je jako gadające narzędzie, a nie "osobę". Nie zadawajcie mu pytań, na które sami możecie…” |
| 5 | **Poland's place in the AI race**<br>Polska w wyścigu AI: zacofanie czy szansa | objection | regulation_politics | 178 | 3.0% | 5 | youtube=178 | 25% | 3 | „Polska nie ma szans na rozwój AI nie mamy taniej energii a firmy nie wymagają aż tak zaawansowanych komputerów ze względu na prymitywizm naszego przemysłu. Usł…” |
| 6 | **ChatGPT relationships: attachment, sycophancy, replacing pe…**<br>Relacje z ChatGPT: przywiązanie, lizusostwo, zastępowanie l… | fear | everyday_use | 155 | 2.6% | 6 | youtube=155 | 49% | 3 | „przeraża mnie to jak bardzo ugodowy jest chociażby chat gpt, oczywiście jeśli napiszesz mu jakąś totalną głupotę to cię poprawi, ale gdy napiszesz mu np. że ka…” |
| 7 | **Fatalism: AI will doom humanity**<br>Fatalizm: AI doprowadzi do zagłady ludzkości | fear | ai_safety_xrisk | 138 | 2.3% | 8 | youtube=138 | 16% | 4 | „wszyscy sie jaraja ale malo kto zdaje sobie sprawe, ze te rozważania i dzialania w tym kierunku mogą nas doprowadzić do katastrofy. NIKT nie wie gdzie prowadzi…” |
| 8 | **Is AI just another technological revolution?**<br>Czy AI to kolejna rewolucja technologiczna? | argument_for | other | 130 | 2.2% | 10 | youtube=130 | 19% | 3 | „Ja rozumiem, że kiedyś ludzie "rzucali kamieniami" w silnik spalinowy z obawy, że odbierze im pracę. Ale nie oszukujmy się rewolucja, która nadchodzi to nie je…” |
| 9 | **Discrediting AI pundits' expertise and motives**<br>Podważanie autorytetu ekspertów od AI | objection | capabilities_hype | 117 | 1.9% | 7 | youtube=117 | 25% | 4 | „Eh, przestańcie już stawić Dragana jako autorytet w tej dziedzinie. Bez dwóch zdań, jest on ekspertem z fizyki, ale jeśli chodzi o informatykę i AI to zwyczajn…” |
| 10 | **AI will doom humanity — via human nature**<br>AI zniszczy ludzkość — przez ludzi, nie sama | fear | ai_safety_xrisk | 112 | 1.9% | 9 | youtube=112 | 27% | 3 | „To nie pistolet zabija człowieka, ale człowiek naciskający spust, to nie bomby atomowe zabiły ludzi w Japonii, ale ludzie planujący i wykonujący nalot i to nie…” |
| 11 | **Humanoid robots: replacing or subjugating humans**<br>Humanoidalne roboty: zastąpią nas czy zniewolą? | fear | jobs_economy | 72 | 1.2% | 13 | youtube=72 | 11% | 3 | „Rozwój mechanicznych robotów idzie i w tą stronę, żeby dały radę zrobić wszystkie manualne rzeczy, które ludzie robią. Zaczynali od przerzucania paczek w magaz…” |
| 12 | **AI as the next stage of evolution**<br>AI jako kolejny etap ewolucji | argument_for | ai_safety_xrisk | 65 | 1.1% | 12 | youtube=65 | 18% | 4 | „Moje przemyślenie jest takie, że człowiek to tylko jedno z ogniw łańcucha ewolucji, które przeminie tak jak przeminęli neandertalczycy, denisowianie, czy inne …” |
| 13 | **Kids turning to AI instead of people**<br>Dzieci i młodzież rozmawiające z AI zamiast z ludźmi | argument_for | health | 62 | 1.0% | 11 | youtube=62 | 63% | 4 | „Myślę, że ludzie patrzący na to z tej perspektywy (poniekąd zdrowej i sensownej) są kompletnie odklejeni od realiów, w jakich żyją wspomniane dzieciaki. Ten ws…” |
| 14 | **AI progress pace: revolution or bubble?**<br>Tempo rozwoju AI: rewolucja czy bańka? | argument_for | capabilities_hype | 58 | 1.0% | 14 | youtube=58 | 16% | 3 | „Game Over. To co jeszcze pół roku temu AI robiła słabo dziś robi niemal bezbłędnie. Rok temu myśl że AI zakoduje grę wzbudzała "taa, może za 5 lat" a tym czase…” |
| 15 | **AI replacing doctors amid healthcare frustration**<br>AI zamiast lekarzy – frustracja służbą zdrowia | argument_for | health | 55 | 0.9% | 16 | youtube=55 | 24% | 4 | „Sorry, ale porady lekarskie są obarczone większym ryzykiem błędu, np. w zestawianiu leków, niż porady AI. Takie marudzenie, jakby ludzie byli nieomylni, a tymc…” |
| 16 | **Can AI be conscious or have a soul?**<br>Czy AI może mieć świadomość lub duszę? | misconception | capabilities_hype | 53 | 0.9% | 18 | youtube=53 | 30% | 4 | „Świadomość jest cechą duszy. Dusza pochodzi ze świata duchowego a nie z AI. AI nigdy nie osiągnie świadomości. Kropka” |
| 17 | **Superintelligence escaping control, threatening humanity**<br>Superinteligencja wymknie się spod kontroli i zagrozi ludzk… | fear | ai_safety_xrisk | 52 | 0.9% | 17 | youtube=52 | 29% | 4 | „Chyba rozmawiamy już o dwóch różnych rzeczach. Ty opisujesz zagrożenia wynikające z ludzkiej głupoty, fanatyzmu czy koncentracji władzy — i z tym trudno się ni…” |
| 18 | **AI cybersecurity, sandbox escapes, data privacy**<br>AI, cyberbezpieczeństwo, ucieczki z sandboxa i prywatność d… | fear | privacy_surveillance | 49 | 0.8% | 15 | youtube=49 | 24% | 3 | „Testy bezpieczeństwa: Laboratoria takie jak OpenAI i Anthropic testowały modele AI pod kątem cyberbezpieczeństwa i zadań hakerskich w odizolowanych środowiskac…” |
| 19 | **Are LLMs just statistics or real thinking?**<br>Czy LLM to tylko statystyka, czy myślenie? | misconception | capabilities_hype | 45 | 0.7% | 19 | youtube=45 | 16% | 4 | „Teraz trochę faktów :AI nie rozumie znaczenia tylko korelacjie jest to zaawansowana analiza statystyczna, po prostu przewiduje słowa, które pasują do pytania n…” |
| 20 | **Pull the plug: shut off power/internet**<br>Wyłączyć prąd/internet, by zatrzymać AI | misconception | ai_safety_xrisk | 43 | 0.7% | 21 | youtube=43 | 30% | 4 | „Powinniśmy mieć jakąś jedną wtyczkę, która wyłączy prąd na całym świecie, by w razie czego zresetować AI😊” |
| 21 | **Jokes, mockery and indifference toward AI**<br>Żarty, kpiny i obojętność wobec AI | joke_cynicism | other | 40 | 0.7% | 20 | youtube=40 | 18% | 2 | „Ja - Zrób coś dla mnie AI - Zrobione! Ja - Ej, ale to jest spieprzone! AI - Masz rację, to jest spieprzone! Tak działa AI :)” |
| 22 | **Dispute: rational fear or fearmongering**<br>Spór: rozsądny strach czy propaganda strachu | objection | ai_safety_xrisk | 38 | 0.6% | 24 | youtube=38 | 21% | 2 | „Ja uważam odwrotnie - to właśnie ci, którzy uspokajali przyczyniali się do uśpienia czujności, a to mało rozsądne nie bać się czegoś czego się nie rozumie, co …” |
| 23 | **Scattered conversational replies about AI**<br>Luźne repliki w dyskusjach o AI | argument_for | other | 37 | 0.6% | 28 | youtube=37 | 14% | 1 | „A czy nie wystarczy tylko wyciągnąć wtyczkę?” |
| 24 | **AI as nuclear bomb: arms race, weapons**<br>AI jak bomba atomowa: wyścig zbrojeń i broń | fear | ai_safety_xrisk | 36 | 0.6% | 27 | youtube=36 | 22% | 4 | „To wygląda jak wyścig zbrojeń o pierwszą bombę atomową, kto będzie pierwszy i skuteczny nie bacząc na skutki. Dokładnie tak samo AI z USA robi wszystko bez zah…” |
| 25 | **What is intelligence versus wisdom?**<br>Czym jest inteligencja, a czym mądrość? | argument_for | ai_safety_xrisk | 35 | 0.6% | 25 | youtube=35 | 23% | 3 | „A w tym czasie jakas mafia lub sekta cichaczem... A w sumie dlaczego obawiac się inteligencji? Wolisz miec mądrych czy glupich znajomych? Czasami myslę , ze lu…” |
| 26 | **AI agents: grammar, jobs, trust**<br>Agenci AI: język, praca, zaufanie | joke_cynicism | everyday_use | 32 | 0.5% | 26 | youtube=32 | 19% | 2 | „1:02 - "budują agenty", a nie "agentów". Boty i automaty to agenty, natomiast żywi ludzie to agenci.” |
| 27 | **AI extinction, aliens, cosmic speculation**<br>AI jako zagłada, kosmos, UFO i koniec ludzkości | fear | ai_safety_xrisk | 32 | 0.5% | 29 | youtube=32 | 28% | 3 | „​​ że stwierdzi że człowiek przeszkadza w czymś jej modelowi świata. Tak jak człowiek wymordował w historii miliony swoich pobratymców. AI potrzebuje ogromnych…” |
| 28 | **Arguments over how AI models really work**<br>Spory o to, jak naprawdę działają modele | objection | capabilities_hype | 31 | 0.5% | 30 | youtube=31 | 23% | 2 | „Przestańcie wypisywać bzdury. Od dwóch lat tworzę "struktury fizyki systemu" dla modeli. I tacy KLAUNI mówią o bezpieczeństwie w momencie jak nie mają nic do p…” |
| 29 | **Terminator is becoming a documentary**<br>Terminator staje się filmem dokumentalnym | joke_cynicism | ai_safety_xrisk | 30 | 0.5% | 22 | youtube=30 | 27% | 5 | „Za późno. Terminator to był film na faktach.” |
| 30 | **AI as elite tool for enslaving people**<br>AI jako narzędzie elit do zniewolenia ludzi | fear | big_tech_power | 30 | 0.5% | 23 | youtube=30 | 20% | 3 | „Kasta bogatych społeczeństw otrzymuje doskonałe narzędzie do kontrolowania i zarządzania resztą ludzkości. Ta reszta ludzkości zgodzi się na to bez sprzeciwu w…” |

## 2. Questions to answer, by theme

Top 15 themes by size. Questions are inferred ("what would this person need to hear?"), not quoted. ⚠️ marks AI-safety / x-risk.

### 1. AI job loss enriches corporations, impoverishes workers — *AI zabiera pracę, zyskują korporacje i elity*
Commenters largely believe AI is already being used by corporations to cut jobs and costs, concentrating wealth among owners while causing unemployment, falling wages and social stratification, with some asking who will buy products if everyone is jobless.  
`fear` · `jobs_economy` · 521 texts

- **Jeśli firmy zastąpią ludzi AI, to kto będzie kupował ich produkty i kto zapłaci podatki?** — If companies replace people with AI, who will buy their products and who will pay taxes? `jobs_economy`
- **Czy państwo ma jakiś plan, żeby zyski z AI nie trafiały tylko do właścicieli wielkich firm?** — Does the state have a plan so that AI profits don't go only to the owners of big companies? `regulation_politics`
- **Które zawody naprawdę już tracą pracę przez AI i co mogą zrobić ludzie, którzy zostaną zwolnieni?** — Which jobs are really being lost to AI already, and what can people who get laid off do? `jobs_economy`

<details><summary>Representative quotes</summary>

> U mnie w firmie lekko polowa ludzi została wywalona. Niby koszty, rezim budzetowy itp ale wiadomo, AI zmienilo to jak sie pracuje. Czesc ludzi niepotrzebna, a firma rosnie. I to calkiem sporo bo o ok 20%. Wiec z polowa ludzi +AI firma moze zarobic 20% RDR. I to nie jest odosobniony przypadek, wiele organizacji tak postepuje. Zastanawia tylko to, jak juz tak pozwalniaja ludzi, zoptymalizuja procesy pod AI to kto bedzie kupowal produkty, uslugi tych organizacji skoro tak wielu bedzie bezrobotnych? ([link](https://www.youtube.com/watch?v=S4ORwO1h5Bk&lc=UgzkJF3OYDVToTG99wt4AaABAg))

> Moim zdaniem, głównymi beneficjentami AI będą właściciele kapitału, firm i akcjonariusze. Już teraz mamy do czynienia z sytuacją, że juniorów w IT zastępuję się narzędziami AI, które obsługują seniorzy. ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgyJ95p9ACSx8DLmss54AaABAg))

> Jeżeli są osoby, które nadal myślą że AI to samo dobro to współczuję. Netto będzie bezrobocie, większa bieda, koncerny jeszcze bogatsze. Rozwarstwienie społeczne. ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgwqGORzSKHbd5ZIlLt4AaABAg))

> Warto zauważyć o czym prawie NIKT nie mówi, otóż ci którzy mają robotę, gdzie AI niby nie grozi, czy nawet robotyzacja, jak hymm wykończeniówka mieszkań, tez oberwą. Dlaczego? Ponieważ jeżeli zaraz z 20-30% osób straci pracę (a kiedyś moze i z 80%), to gdzie oni pójdą, jak nie do zawodów, gdzie AI i robotyzacja nie grozi? Pójdą do waszych zawodów i będą konkurencją na rynku pracy. Nawet jak roboty nie stracicie, to zarobki spadną, żelazne prawo podaży i popytu. Poza tym ile osób moze pracowac w… ([link](https://www.youtube.com/watch?v=NUWJufnbtjQ&lc=UgxMvsbXHrbtsMebPiN4AaABAg))

</details>

### 2. Mass unemployment: who will buy anything? — *Masowe bezrobocie: kto kupi, gdy nikt nie zarabia?*
Commenters fear AI-driven mass layoffs will collapse consumer demand and spill over even to manual trades, while corporations and capital owners capture the gains and leave most people poorer, with deep scepticism that UBI or goodwill from tech firms will fix it.  
`fear` · `jobs_economy` · 448 texts

- **Jeśli AI zabierze pracę biurową dużej części ludzi, to kto będzie płacił za usługi fachowców i kupował produkty firm?** — If AI takes office jobs from a large share of people, who will pay for tradespeople's services and buy companies' products? `jobs_economy`
- **Czy dochód podstawowy albo inne rozwiązania są realne, czy zyski z AI po prostu trafią do kilku korporacji?** — Is a basic income or other solution realistic, or will AI profits just go to a few corporations? `big_tech_power`
- **Co państwo i regulacje mogą zrobić, żeby szybka automatyzacja nie zwiększyła drastycznie nierówności?** — What can the state and regulation do so that rapid automation doesn't drastically increase inequality? `regulation_politics`

<details><summary>Representative quotes</summary>

> Już teraz tak jest. Pracownicy są zwalniani, zespoły redukowane. Tylko kto kupi produkty firm jeśli nikt nie będzie miał pieniędzy? ([link](https://www.youtube.com/watch?v=DT_VvKTXyTI&lc=UgxLxjFVDGluUdPNi3h4AaABAg))

> Ludzie nie będą mieć pracy = budowlańcy nie będą mieli sami roboty. Sedno całego problemu jest takie że spora osób podchodzi do tego na zasadzie "mnie to nie dotknie bo nie jestem programistą, grafikiem" czy innym podobnym. Tylko że oni też nie żyją w próżni - są zależni od tego czy ktoś ma pieniądze żeby korzystać z ich usług. ([link](https://www.youtube.com/watch?v=NUWJufnbtjQ&lc=UgxMvsbXHrbtsMebPiN4AaABAg.AcuwJy7GPGPAcvCbUg2CbI))

> Ale wiesz, że gdy ludzie, którzy siedzą za biureczkiem, na przestrzeni kilku lat masowo stracą pracę, to przestaną płacić za produkty i usługi tych świadczących "prawdziwą pracę" i wszyscy zaczną piszczeć z biedy, a państwo będzie zmuszone dopłacać dużo, duuużo więcej z podatków tych, którzy zostali na powierzchni? Czy może wydaje ci się, że wszyscy, łącznie z 50-letnimi Grażynkami z urzędów, z dnia na dzień zostaną lekarzami, fryzjerami i glazurnikami i jakoś to będzie;)? ([link](https://www.youtube.com/watch?v=cNrpt4GgE28&lc=UgxEQ8s1d1vYirj0OpN4AaABAg.AanQyiD-XFaAaoFQH6Vvki))

> czym - obok tych, którzy dziś zajmują się pracą manualną, pojawi się milion innych, którzy zostaną bez pracy i będą się przebranżawiać na tego typu zajęcia . Ogólnie rozwarstwienie społeczeństwa będzie jeszcze większe i szybciej nastąpi, aniżeli obserwowaliśmy to do tej pory. Aktualni posiadacze kapitału będą go mieć jeszcze więcej. A reszta nas? Strach się bać. ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgzpAYbRXRR5Z9713z14AaABAg.ALOUC322i_eALPprj6MgEB))

</details>

### 3. Scattered sarcastic quips about AI — *Sarkastyczne, rozproszone komentarze o AI*
A grab-bag of short, mostly sarcastic or cynical one-liners reacting to AI videos — mocking doom warnings, distrusting AI insiders, joking about power plugs and enslavement, with occasional stray worries about privacy leaks and jobs.  
`joke_cynicism` · `ai_safety_xrisk` · 447 texts

- **Czy ostrzeżenia ludzi z OpenAI i innych firm o zagrożeniach AI to szczera troska, czy marketing?** — Are warnings about AI risks from people at OpenAI and other companies sincere concern or marketing? `big_tech_power`
- ⚠️ **Czy nie wystarczy po prostu wyłączyć prąd, jeśli AI wymknie się spod kontroli?** — Couldn't we just pull the plug if AI gets out of control? `ai_safety_xrisk`
- **Czy to, o co pytam czatbota, może kiedyś wyciec i zostać użyte przeciwko mnie?** — Could what I ask a chatbot leak someday and be used against me? `privacy_surveillance`

<details><summary>Representative quotes</summary>

> Hodują ai? Teraz to juz ona nas hoduje ([link](https://www.youtube.com/watch?v=Ke1wYfi6xJs&lc=UgyGyV0P42u0yYN7qep4AaABAg))

> Bzdury… Będą jakieś „incydenty” i tyle (co jakiś czas odwala jakiś numer i tyle). Rozluźnić pośladki! ([link](https://www.youtube.com/watch?v=r_I6bfxtmLg&lc=UgziQ-p49cjZqAfiCf94AaABAg))

> Serio? Jak na to wpadliscie? Wooow! Zaglada i zniewolenie nadchodzi. Globalne ([link](https://www.youtube.com/watch?v=Si6xhigObEY&lc=UgwW3eaxUkv6Q63yl4l4AaABAg))

> Jelenie uwierzą, że Pan z open ai powie prawdę o open ai ([link](https://www.youtube.com/watch?v=qaT3MXdBXDo&lc=Ugy9MBXxbfH5a6WYCBV4AaABAg.Ad-aYQCRotlAdElpnZPw3s))

</details>

### 4. AI is just a tool that makes mistakes — *AI to tylko narzędzie – popełnia błędy*
Commenters largely frame AI as a mere (often error-prone, sycophantic) tool or 'language calculator' without real understanding or consciousness, to be used with distance and verification, while a minority counter that a tool gaining agency could escape control.  
`argument_for` · `capabilities_hype` · 336 texts

- ⚠️ **Czy AI to naprawdę tylko narzędzie jak młotek, czy może zacząć działać samodzielnie?** — Is AI really just a tool like a hammer, or can it start acting on its own? `ai_safety_xrisk`
- **Dlaczego chatboty tak często się mylą i przytakują mi, gdy zwracam im uwagę, i jak sprawdzać ich odpowiedzi?** — Why do chatbots so often make mistakes and just agree with me when I correct them, and how should I verify their answers? `everyday_use`
- **Czy modele językowe coś rozumieją, czy tylko przewidują słowa?** — Do language models understand anything, or do they just predict words? `capabilities_hype`

<details><summary>Representative quotes</summary>

> I jeśli mógłbym udzielić jakiejś wskazówki, dotyczącej AI: traktujcie je jako gadające narzędzie, a nie "osobę". Nie zadawajcie mu pytań, na które sami możecie znaleźć odpowiedzi. To nie tylko rozleniwia Was samych, ale też sprawia, że zbytnio ufacie temu rozbudowanemu algorytmowi, który może być "karmiony" przez każdego, kto ma dostęp do sieci. I w efekcie w końcu zacząć udzielać odpowiedzi zupełnie niezgodnych z prawdą. Ja osobiście używam klientów AI jedynie do tworzenia grafik, bo sam rysow… ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=UgzKn7f76eE63exTEMt4AaABAg))

> Używam AI do programowania. Gdyby nie ona straciłbym motywację i porzucił projekt. Dzięki temu małymi kroczkami posuwam się do przodu. Ale co ważne - jestem świadomy z popełniania błędów przez AI. Traktuje ją tak, jak wypowiedzi na jakiś forach. Przecież nie zawsze ktoś dobrze Ci podpowie lub doradzi. Trzeba mieć dystans. ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=UgxYlw3ueE97KEef93J4AaABAg))

> Do wyników pracy AI nie tylko nie należy podchodzić bezkrytycznie ale wręcz trzeba ją sprawdzać. AI nie tylko popełni błąd ale jak zwrócisz mu na to uwagę to bardzo często zgodzi się z Tobą, poinformuje Cię że ponownie przeanalizowało wyniki a na koniec wypluje to samo lub co najwyżej z innym błędem. ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=UgwArF2ycb0zUuWuUeh4AaABAg))

> Zwykły program komputerowy, dajmy na to symulacja galaktyki, wykonuje zadania, których żaden człowiek nie jest w stanie wykonać, co nie oznacza, że ten program ro jest jakaś inteligencja. To jest automat taki sam jak AI. Oczywiście są różnice ale czego byś nie mówił wszystko co robi AI jest tylko i wyłącznie skutkiem zachodzących w niej procesów i nijak żadnego rozumu tam być nie może. Ciężarówka też rozwiązuje problemy, których żaden człowiek nie potrafi, chociaż prawda, nie są one matematyczn… ([link](https://www.youtube.com/watch?v=ri-fv-6FSxY&lc=UgxKsM3Hxwh2Ah9tWVp4AaABAg.A_wD_1iFR4LA_wopXe3Y8y))

</details>

### 5. Poland's place in the AI race — *Polska w wyścigu AI: zacofanie czy szansa*
Commenters debate Poland's position in AI, mostly cynically asserting that Poland is backward, unprepared, hampered by politicians and a 'assembly-plant mentality', and merely exports talent to US firms, while a minority defends Polish models (Bielik, PLLuM) and startups or questions whether the startups touted as 'Polish' really are.  
`objection` · `regulation_politics` · 178 texts

- **Czy Polska ma realne szanse w rozwoju AI, skoro nie mamy taniej energii ani wielkich pieniędzy jak USA czy Chiny?** — Does Poland have any real chance in AI development without cheap energy or the big money of the US or China? `regulation_politics`
- **Czy polskie modele jak Bielik czy PLLuM mają sens, skoro amerykańskie modele są lepsze?** — Do Polish models like Bielik or PLLuM make sense when American models are better? `capabilities_hype`
- **Co Polska powinna zrobić, żeby zdolni informatycy nie wyjeżdżali pracować dla amerykańskich korporacji?** — What should Poland do so talented engineers don't just end up working for American corporations? `big_tech_power`

<details><summary>Representative quotes</summary>

> Polska nie ma szans na rozwój AI nie mamy taniej energii a firmy nie wymagają aż tak zaawansowanych komputerów ze względu na prymitywizm naszego przemysłu. Usługi wyjdą z Polski do Indii i innych krajów a u nas dochodzi już do zwolnień ([link](https://www.youtube.com/watch?v=TW7g2Yj8wPQ&lc=UgyVXRKC5ZUA8qV77SV4AaABAg))

> Jednym z problemów Polski jest mentalność montowni, ukształtowana na początku lat 90-tych z której nie moźemy jakoś się wyzwoliċ. Uczelnie wyższe zamienia się w zawodówki a aspiracje ludzkie kształtuje się celując w pracę w korpo i zdolnośċ kredytową (te ostatnie same w sobie nie są złe - ale marzenia, które popychają ludzi do nadzwyczajnych powinny być większe). W edukacji toczymy XIX-wieczne wojny a rządzić nią pozwalamy ideologom. W Stanach akurat nie jest z tym lepiej - ale tam, na końcu i … ([link](https://www.youtube.com/watch?v=fo3BRFjuiQ0&lc=Ugz47yV1ZQ4Rid2gypp4AaABAg))

> Fantastycznie, że jesteśmy kuźnią talentów informatycznych dla amerykańskiej gospodarki. Jest się z czego cieszyć ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=Ugyv_M5qcQpmRRVHb4F4AaABAg))

> Nie prawda nie trzymają poziomu. Słabo się przygotowali w kwestii AI w Europie i w Polsce. Nie zadawali niewygodnych pytań. Tylko potakiwali gościowi, który ma słabe pojęcie co tu (w kraju i Europie) się dzieje odnośnie AI. I tak Europa już się obudziła i inwestuje w AI. Gość powiela tylko dawne przekonanie, że Europa śpi. Prowadzący ani słowem nie wspomnieli o polskich modelach językowych (Bielik, Pllum), a chyba powinni o nich wiedzieć, albo dowiedzieć przygotowując się do rozmowy. Nie wspomn… ([link](https://www.youtube.com/watch?v=vfiCcI8uWlM&lc=Ugxz10RJIdwLBXGRJVl4AaABAg.Acq5zoi5mqtAcsIpu3mpK3))

</details>

### 6. ChatGPT relationships: attachment, sycophancy, replacing people — *Relacje z ChatGPT: przywiązanie, lizusostwo, zastępowanie ludzi*
Commenters debate personal, often emotional use of ChatGPT as a conversation partner — some embrace it as a better, kinder interlocutor than people, while many worry about its flattering, agreeable sycophancy, emotional dependence, and the substitution of real human relationships.  
`fear` · `everyday_use` · 155 texts

- **Dlaczego ChatGPT tak często przyznaje mi rację i mi schlebia — czy to celowe, żebym go częściej używał?** — Why does ChatGPT so often agree with and flatter me — is it deliberate to keep me using it? `big_tech_power`
- **Czy przywiązanie emocjonalne do chatbota jest szkodliwe i jak rozpoznać, że zastępuje mi on prawdziwe relacje?** — Is emotional attachment to a chatbot harmful, and how can I tell it's replacing my real relationships? `health`
- **Jak ustawić lub prosić AI, żeby dawało mi szczerą krytykę zamiast przytakiwania?** — How can I set up or prompt AI to give me honest criticism instead of just agreeing? `everyday_use`

<details><summary>Representative quotes</summary>

> przeraża mnie to jak bardzo ugodowy jest chociażby chat gpt, oczywiście jeśli napiszesz mu jakąś totalną głupotę to cię poprawi, ale gdy napiszesz mu np. że karmisz kota whiskas i wszyscy się ciebie czepiają, a przecież twój kot tak lubi te karmę, to on weźmie twoją stronę, czasem coś mimochodem wspomni o szkodliwości karmy, ale zgodzi się z tobą, a ostatecznie z rozmowy wyniknie że w sumie to nic złego nie robisz i tak trzymaj. kiedyś wrzuciłam do chata dokładnie te samą rozmowę dwa razy, na d… ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=UgzOXVgIcUrZbApTURt4AaABAg))

> Ja jestem jedną z tych osób co po wyłaczeniu gpt 4o i zastąpieniu go gpt5 płakała przez cały dzień xD. I w moim odczuciu ciężko się jest do takiego bota nie przywiązywać. Ludzie potrafią wytworzyć sztuczną relację z aktorem, którego nigdy nie poznali albo z postacią z anime, której nigdy nie będą w stanie poznać. Więc nie widzę w tym absolutnie nic dziwnego, że ludzie łatwo się przywiazują do takiego bota, który reaguję na nasze indywidualne potrzeby, nie ocenia i zawsze odpowie. Jednak wiadomo… ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=UgxjARzJIhRD5GVKcqN4AaABAg))

> Masz cały yt, fora dyskusyjne online I wiele wiele innych a i tak wolisz gadać z botem. Nawet nie widzisz jak to jest szkodliwe i dla psychiki i poznawczo. Dyskusja polega na wymianie informacji. Twój rozmówca nie musi się z tobą zgadać, wystarczy że będzie kulturalny. I to dotyczy też ciebie. Social media zatomizowały nas i wmówiły że różnice to zło. Boty tylko nas dobiją. Prawdziwa przyjaźń czy związek polegają na tym że umiesz powiedzieć tej drugiej osobie "nie zgadzam się", "robisz to źle" … ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=Ugw4qQGxOXStWhbj3DR4AaABAg.AM6ywlOexjzASCRU8eNKM_))

> Ja to bym jednak skłaniała się ku temu, że Chat GPT jest właśnie zbyt miły. Czasem gdy chcę, żeby mi coś przeanalizował to chciałbym ocenę bez tego całego słodzenia. Nawet jak piszę, żeby nie słodził to widać, że powstrzymuje się przed krytyką. ([link](https://www.youtube.com/watch?v=5ka0VwglHrY&lc=UgzJ1iJEFvQDxkkxhh94AaABAg))

</details>

### 7. Fatalism: AI will doom humanity — *Fatalizm: AI doprowadzi do zagłady ludzkości*
Commenters overwhelmingly express doom-laden fatalism that AI will destroy, enslave or replace humanity, often blaming human greed, short-sightedness or a "self-destruction gene" for pushing ahead anyway, with some religious and conspiratorial framings and a few resigned jokes.  
`fear` · `ai_safety_xrisk` · 138 texts

- ⚠️ **Czy naprawdę jest już za późno, żeby zatrzymać lub kontrolować rozwój AI, czy wciąż możemy coś zrobić?** — Is it really too late to stop or control AI development, or can we still do something? `ai_safety_xrisk`
- **Skoro sami twórcy przyznają, że nie rozumieją swoich modeli, to dlaczego wciąż je rozwijają i kto ich może powstrzymać?** — If the creators admit they don't understand their models, why do they keep building them and who can stop them? `regulation_politics`
- ⚠️ **Co zwykły człowiek może zrobić, żeby AI nie odebrała ludziom wolności i kontroli nad własnym losem?** — What can an ordinary person do so that AI doesn't take away people's freedom and control over their fate? `ai_safety_xrisk`

<details><summary>Representative quotes</summary>

> wszyscy sie jaraja ale malo kto zdaje sobie sprawe, ze te rozważania i dzialania w tym kierunku mogą nas doprowadzić do katastrofy. NIKT nie wie gdzie prowadzi ta królicza nora ([link](https://www.youtube.com/watch?v=QalHlv3LbuY&lc=Ugx2ncCRME39-rRYZrp4AaABAg.APK7HPYYbefAPOkwTrMFNh))

> To jak w filmie dont look up . Mówi nam się żebyśmy nie patrzyli w górę i może jeszcze da się zatrzymać ai ale chciwość garstki na to nie pozwoli więc jedyne co możemy zrobić to patrzeć jak leci do nas ai które nas zniszczy. Wmawiają nam że nie ma problemu i spora część ludzkości im wierzy a my możemy tylko patrzeć jak niszczą ten świat... ([link](https://www.youtube.com/watch?v=Ke1wYfi6xJs&lc=Ugy3PdrH0_5f-VkClMR4AaABAg))

> Są rzeczy do których się nie zaadaptujemy. Gdy zmagamy się z czymś nieskończenie mądrzejszym od siebie, jedyne co nas czeka to nieodwołalna zagłada ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgyHMQW-hQNupif1SVh4AaABAg.ALNA1juwDseALNCFHTOevq))

> Już utraciliśmy kontrolę, tylko jeszcze nie wszyscy o tym wiedzą. ([link](https://www.youtube.com/watch?v=Ke1wYfi6xJs&lc=UgyabITc4DSkMASyBsZ4AaABAg))

</details>

### 8. Is AI just another technological revolution? — *Czy AI to kolejna rewolucja technologiczna?*
Commenters debate whether AI is comparable to past technological revolutions (steam, electricity, internet) that ultimately benefited humanity, or a fundamentally different shift that replaces human thinking itself and, like recent tech, fails to improve ordinary people's lives.  
`argument_for` · `other` · 130 texts

- ⚠️ **Czy AI to po prostu kolejna rewolucja jak maszyna parowa czy internet, czy coś zupełnie innego, bo zastępuje samo myślenie?** — Is AI just another revolution like the steam engine or the internet, or something fundamentally different because it replaces thinking itself? `ai_safety_xrisk`
- **Skoro mamy coraz lepszą technologię, a i tak musimy pracować więcej, żeby przeżyć, to kto naprawdę skorzysta na AI?** — If technology keeps improving yet we still have to work more to get by, who will actually benefit from AI? `jobs_economy`
- **Czy da się spowolnić lub ukierunkować rozwój AI, jeśli przestaje on służyć ludziom?** — Can AI development be slowed down or steered if it stops serving people? `regulation_politics`

<details><summary>Representative quotes</summary>

> Ja rozumiem, że kiedyś ludzie "rzucali kamieniami" w silnik spalinowy z obawy, że odbierze im pracę. Ale nie oszukujmy się rewolucja, która nadchodzi to nie jest ta sama, którą w poprzednich wiekach przeżywali nasi przodkowie. Maszyny myślące kilka kroków do przodu? Inteligentniejszą od człowieka? Myślę, że w przyszłości kwestia likwidacji stanowisk pracy, czy używanie sobie do woli cudzych dzieł intelektualnych będzie najmniej dotkliwym z problemów ludzkości. Oddajmy modelom wszystkie dane na … ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgxT14lCF783rkm8mXJ4AaABAg))

> 200 lat temu: 90% ludzi pracuje w rolnictwie. Dziś: 3% ludzi pracuje w rolnictwie. Ludzkość nie wyginęła, świat się nie zawalił, a żyjemy w najlepszym momencie w historii. Automatyzacja nie likwiduje ludzi – likwiduje nieefektywność. Kolejny przeskok techniczny i tyle. ([link](https://www.youtube.com/watch?v=405KjGtT-Do&lc=Ugyq4kOd-_tETXSN8eV4AaABAg))

> Tak samo ludzie biadolili gdy pojawiły się maszyny parowe i elektryczność. Zamiast biadolić, trzeba myśleć jak optymalnie wykorzystać tę szansę, bo świat na nas czekać nie będzie.To są nieuniknione zmiany, na tym polega ewolucja, przystosuj się albo giń. ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgyJ95p9ACSx8DLmss54AaABAg.ALNTHr5rrfAALNei4viJvp))

> Porównywanie poprzednich rewolucji, w których tworzono narzędzia, bezmyślne, programowalne najwyżej, będące przedłużeniem umysłu - z osobnym bytem, o większej wiedzy, możliwości samo edukacji, samo organizacji, błyskawicznie ewoluujące, mózgiem sprawniejszym niż nasze jest niedorzeczne. ([link](https://www.youtube.com/watch?v=ri-fv-6FSxY&lc=Ugx6L58GsnZCx0wevzJ4AaABAg))

</details>

### 9. Discrediting AI pundits' expertise and motives — *Podważanie autorytetu ekspertów od AI*
Commenters attack the credibility of public AI commentators (especially physicist Andrzej Dragan, but also OpenAI's Aleksander Mądry, Hinton and others), calling them non-experts, fearmongers or salesmen driven by book sales, stock options or hype, and mocking media for platforming them.  
`objection` · `capabilities_hype` · 117 texts

- **Kto tak naprawdę jest ekspertem od AI i dlaczego media zapraszają fizyków zamiast informatyków?** — Who actually counts as an AI expert, and why do media invite physicists instead of computer scientists? `other`
- ⚠️ **Skoro nawet laureaci Nagrody Turinga, jak Hinton i LeCun, się nie zgadzają, to komu wierzyć w sprawie zagrożeń AI?** — If even Turing Award winners like Hinton and LeCun disagree, whom should we believe about AI risks? `ai_safety_xrisk`
- **Czy ostrzeżenia o zagrożeniach AI to nie jest po prostu marketing firm i autorów, którzy na tym zarabiają?** — Aren't warnings about AI dangers just marketing by companies and authors who profit from them? `big_tech_power`

<details><summary>Representative quotes</summary>

> Eh, przestańcie już stawić Dragana jako autorytet w tej dziedzinie. Bez dwóch zdań, jest on ekspertem z fizyki, ale jeśli chodzi o informatykę i AI to zwyczajnie pieprzy. Od kilka lat widzę, że stawia AI w roli terminatora i straszy ludzi, możliwe przez to, że chce zrobić szum i opublikować kolejna książkę. Lata mijają, a wszystko co mówił, się nie sprawdziło, to zwykły populista jeśli chodzi o informatykę ([link](https://www.youtube.com/watch?v=V4VREmXMYDU&lc=UgxueWjhJciAliNc1kV4AaABAg))

> Naprawdę nie brakuje dziś fachowców, którzy znają AI od podszewki — ludzi z ogromną wiedzą techniczną i praktycznym doświadczeniem. A jednak zapraszacie pana Dragana. Być może jest świetnym fizykiem, ale w temacie sztucznej inteligencji wypowiada się jak amator: doszukuje się sensacji tam, gdzie jej zwyczajnie nie ma. Przy kolejnym materiale zachęcam do szerszego researchu i doboru rozmówców, którzy wnoszą merytorykę, a nie rozpoznawalność. Zamiast kolejnego wywiadu z celebrytą, potrzebny jest … ([link](https://www.youtube.com/watch?v=zdSqTtQHjAc&lc=Ugxhfe9JewVEXc-S_cp4AaABAg))

> Dragan skutecznie straszy sztuczną inteligencją od kilku lat, żeby to zmonetyzować wydając książkę. Już kilka razy przewidywał koniec świata i się nie sprawdziło. ([link](https://www.youtube.com/watch?v=V4VREmXMYDU&lc=UgzTmXJGhsk-u5f-2Wx4AaABAg))

> Nalezy mieć na uwadze że Pan Mądry jest pracownikiem OpenAI i na pewno jest posiadaczem sporego pakietu opcji na akcje.. reszty można się domyśleć a dodając do tego że jest niewiatpliwie bardzo inteligentny człowiek to doskale wie czego mówenie jest dla niego kożystne a czego nie :) ([link](https://www.youtube.com/watch?v=qaT3MXdBXDo&lc=Ugx_i_CfVvGlkihSSBB4AaABAg))

</details>

### 10. AI will doom humanity — via human nature — *AI zniszczy ludzkość — przez ludzi, nie sama*
Commenters broadly expect AI to harm or end humanity, but most locate the danger in human greed, misuse, arms-race logic and self-inflicted dependence/degeneration rather than in AI acting on its own, with a fatalistic or misanthropic undertone (some even welcome AI replacing humans).  
`fear` · `ai_safety_xrisk` · 112 texts

- ⚠️ **Czy większym zagrożeniem jest sama AI, czy ludzie, którzy ją kontrolują i wykorzystują?** — Is the bigger threat AI itself or the people who control and use it? `ai_safety_xrisk`
- **Czy wyścigu o coraz potężniejszą AI naprawdę nie da się już zatrzymać ani spowolnić, tak jak z bombą atomową?** — Is the race for ever more powerful AI truly unstoppable, like the atomic bomb race? `regulation_politics`
- **Czy poleganie na AI sprawi, że ludzie zgłupieją i stracą kontrolę nad własnym życiem?** — Will relying on AI make people dumber and cause them to lose agency over their own lives? `education`

<details><summary>Representative quotes</summary>

> To nie pistolet zabija człowieka, ale człowiek naciskający spust, to nie bomby atomowe zabiły ludzi w Japonii, ale ludzie planujący i wykonujący nalot i to nie Komory gazowe zabiły ludzi, ale ludzie tam świadomie ich wpędzający. Tak samo, AI nie zabierze pracy, nie zniszczy gospodarek, nie doprowadzi do tragedii ludzi, ale ludzie, którzy świadomie tak tego narzędzia użyją. To nie maszyna jest problemem, ale chciwość, brak empatii, zachłanność i bezwzględność elit doprowadzała zawsze i wciąż dop… ([link](https://www.youtube.com/watch?v=himTPjX098w&lc=UgzitpsWjJDnRmLsEcl4AaABAg))

> Za co by się człowiek nie wziął to finalnie potencjał tego wykorzysta przeciwko drugiemu człowiekowi. Te modele AI i pogoń za doskonaleniem ich jest jak kiedyś pogoń za bombą atomową. Tego już nikt nie zatrzyma. ([link](https://www.youtube.com/watch?v=Ke1wYfi6xJs&lc=UgxgagDNgN_1wiU5M0R4AaABAg))

> AI finalnie doprowadzi do degeneracji biologicznej ludzi i do ich wymarcia. Taka będzie oczywista i nieuchronna przyszłość. I to nie jest propaganda strachu, tylko obiektywne przewidywanie, na które nie mamy wpływu, bo kieruje tym logika rozwoju. AI nie będzie świadomie niszczyć ludzi. To ludzie sami oddadzą jej swoją sprawczość, co spowoduje ich biologiczną degenerację, co zresztą i tak już trwa od czasu, kiedy ludzie zaczęli ułatwiać sobie życie zdobyczami cywilizacyjnymi. Widać to nawet po z… ([link](https://www.youtube.com/watch?v=FI_Wv5zxdzk&lc=UgxGbdSUKMwI6i5t2qh4AaABAg))

> Moim zdaniem większym zagrożeniem nie jest świadoma Ai, tylko ai w niewłaściwych rękach i pod ich kontrolą. ([link](https://www.youtube.com/watch?v=himTPjX098w&lc=Ugx-8W7UIl18S0dyZi54AaABAg))

</details>

### 11. Humanoid robots: replacing or subjugating humans — *Humanoidalne roboty: zastąpią nas czy zniewolą?*
Commenters speculate about AI-powered humanoid robots, mostly expecting them to eventually replace manual labour and make humans redundant, with a strand of dystopian fear (robot soldiers/police, Terminator), alongside some enthusiasm for home robots and sceptical jokes about power and breakdowns.  
`fear` · `jobs_economy` · 72 texts

- **Kiedy roboty humanoidalne naprawdę będą w stanie zastąpić hydraulików, budowlańców czy magazynierów?** — When will humanoid robots realistically be able to replace plumbers, builders or warehouse workers? `jobs_economy`
- **Jeśli AI i robotyka zastąpią prawie całą pracę, z czego będą żyli zwykli ludzie i kto o tym zdecyduje?** — If AI and robotics replace almost all work, how will ordinary people live and who decides that? `jobs_economy`
- **Czy roboty z AI mogą zostać użyte jako żołnierze lub policja przeciwko ludziom i czy ktoś to reguluje?** — Could AI-powered robots be used as soldiers or police against people, and is anyone regulating this? `regulation_politics`

<details><summary>Representative quotes</summary>

> Rozwój mechanicznych robotów idzie i w tą stronę, żeby dały radę zrobić wszystkie manualne rzeczy, które ludzie robią. Zaczynali od przerzucania paczek w magazynie, skończą na chirurgach, grabarzach i hydraulikach. Ty jeszcze popracujesz manualnie, ale za 20 lat to już nie wiadomo. ([link](https://www.youtube.com/watch?v=V4VREmXMYDU&lc=UgziXKR125vQGRDNb5F4AaABAg.AP6U3hi3HnaAQM6EhH9S6S))

> Teraz , teraz tak jest ! A myślałeś co będzie za 15 czy 20 lat ? Naprawdę uważasz ze jesteś tak cudownie mądry ze cie robot nie zastąpi? Ty na urlop pewnie chodzisz, robot nie musi. Chorowałeś kiedykolwiek? To lepiej przestań, bo robot nie choruje. Już trochę dotarło.... co czeka nas jako ludzi ? ([link](https://www.youtube.com/watch?v=zJSBW-0Ds8E&lc=UgxRgcJ5c8lSP4A8FsF4AaABAg.ALPayVMBkuxALUsqPTLQZ_))

> jak już pojawią się roboty na takim poziomie technologicznym, że będą potrafiły szpachlować, zmieniać kran itd. to nie będą wam tego robić. wtedy to już będą stać na wieżyczkach strzelniczych a ty będziesz po niewłaściwej stronie muru z drutu kolczastego. oczywiście w imię twojego bezpieczeństwa i świętego spokoju ([link](https://www.youtube.com/watch?v=Sx4CYs4frUI&lc=UgwDIGzNMwUqR3EVcPd4AaABAg))

> Wraz z AGI będzie robotyka więc ludzie będą zbędni do czegokolwiek. ([link](https://www.youtube.com/watch?v=Ke1wYfi6xJs&lc=UgxwwMgXqdTB1dAret94AaABAg.AaKm-LbgJkmAas9UzjkWyX))

</details>

### 12. AI as the next stage of evolution — *AI jako kolejny etap ewolucji*
Commenters frame AI through an evolutionary lens, often fatalistically or even approvingly treating humanity's replacement by a smarter 'new species' as a natural, inevitable succession, while a minority see it as a dangerous competitor or reject the framing.  
`argument_for` · `ai_safety_xrisk` · 65 texts

- ⚠️ **Czy zastąpienie ludzi przez AI to naturalna ewolucja, czy nasz wybór, na który mamy wpływ?** — Is humans being replaced by AI natural evolution, or a choice we can influence? `ai_safety_xrisk`
- ⚠️ **Skoro AI będzie mądrzejsza od nas, to czy w ogóle da się zachować nad nią kontrolę?** — If AI becomes smarter than us, can we keep control over it at all? `ai_safety_xrisk`
- ⚠️ **Czy superinteligentna AI musiałaby konkurować z ludźmi o zasoby, czy mogłaby nas po prostu zostawić w spokoju?** — Would a superintelligent AI have to compete with humans for resources, or could it simply leave us alone? `ai_safety_xrisk`

<details><summary>Representative quotes</summary>

> Moje przemyślenie jest takie, że człowiek to tylko jedno z ogniw łańcucha ewolucji, które przeminie tak jak przeminęli neandertalczycy, denisowianie, czy inne gatunki człowieka. Moim zdaniem koroną ewolucji będzie nasze "dziecko", czyli świadoma sztuczna inteligencja. Nieco "kolorystycznie" można ująć, żę tak jak życie powstało, aby powstała inteligencja biologiczna, tak "zadaniem" inteligencji biologicznej jest zbudować byt od niej doskonalszy - świadomą sztuczną inteligencję. Dopiero ASI będz… ([link](https://www.youtube.com/watch?v=0YmhQeHxsU8&lc=Ugw_DNDcYxegGdFDlD54AaABAg.AZKWzoSB0bdAZL62VjuOCA))

> naturalna kolej rzeczy, jeden gatunek wypiera drugi, a że ten sami tworzymy to poniekąd będzie ludzkości "spuścizna". Mnie to nie przeraża, niech się martwią następnie pokolenia, czy pójdzie to wszystko w tą dobrą, czy inną stronę.. ([link](https://www.youtube.com/watch?v=himTPjX098w&lc=UgxcM7Z5iB83u-xgaaN4AaABAg))

> Ale dlaczego wizję powstania nowego gatunku traktować jako zagrożenie? To fascynująca wizja, że możemy stworzyć byt miliony razy inteligentniejszy od ludzkości. ([link](https://www.youtube.com/watch?v=FI_Wv5zxdzk&lc=UgwYNfj1RkJZGJ48Juh4AaABAg))

> Koniec swiata nie następuje za pstryknięciem palca. Naturalne proces to miliony lat. Tu zapewne nastąpi to szybciej to raczej setki lat by człowiek wyginął lub trafil do rezerwatu. Wyzsza forma inteligencji zajmie miejsce człowieka ([link](https://www.youtube.com/watch?v=V4VREmXMYDU&lc=UgzTmXJGhsk-u5f-2Wx4AaABAg.AP7BtjRcHyEAPY_ETixXMc))

</details>

### 13. Kids turning to AI instead of people — *Dzieci i młodzież rozmawiające z AI zamiast z ludźmi*
Commenters debate AI's harm to children's emotional development, with many arguing that kids prefer AI companions because parents and peers have already failed them, so AI deepens rather than creates the problem, while others call for parental education or age limits.  
`argument_for` · `health` · 62 texts

- **Czy to normalne, że moje dziecko woli rozmawiać z AI niż ze mną albo z rówieśnikami, i kiedy powinienem się tym martwić?** — Is it normal that my child prefers talking to AI over me or peers, and when should I worry? `health`
- **Czy rozmowy z chatbotem mogą pomóc dziecku, które jest gnębione w szkole, czy raczej mu zaszkodzą?** — Can chatbot conversations help a child bullied at school, or will they do more harm? `health`
- **Czy w Polsce powinno być ograniczenie wiekowe dla korzystania z AI, tak jak w niektórych krajach dla mediów społecznościowych?** — Should Poland introduce an age limit for using AI, like some countries do for social media? `regulation_politics`

<details><summary>Representative quotes</summary>

> Myślę, że ludzie patrzący na to z tej perspektywy (poniekąd zdrowej i sensownej) są kompletnie odklejeni od realiów, w jakich żyją wspomniane dzieciaki. Ten wskaźnik przedkładania rozmów z AI nad rozmowy z ludźmi w ich otoczeniu, w tym z rodzicami, nie bierze się wyłącznie z tego, że AI jest super - nie jest, i nawet nastolatkowie to wiedzą, bo brzmi sztywno i kiepsko w wielu kontekstach. Po prostu ludzie w ich otoczeniu są - jakby to ładnie ująć - tak do bani, że nawet samotność jest lepsza ni… ([link](https://www.youtube.com/watch?v=1j29IoHjf7c&lc=Ugzlt1lfUy6CBSuyZEh4AaABAg))

> Jest wiele prawdy w Tym co mówisz. Ale to pokazuje jeszcze jedną rzecz. Że te relacje między ludzkie były już zepsute, zanim się pojawiło to AI. Dlatego dzieci szukają "przyjaciela" w AI, bo nie mogą liczyć na rodziców, bliskich czy kolegów. ([link](https://www.youtube.com/watch?v=1j29IoHjf7c&lc=Ugzvr9sVZ6ZY64r3pFp4AaABAg))

> Siedzę mocno w AI, i uważam że ten materiał o tej technologii pomija jeden ale bardzo kluczowy fakt. To nie jest tak że zdrowa osoba wpada w problemy przez AI. tamten chłopak co popełnił samobójstwo najprawdopodobniej miał wcześniej problemy. I to poważne. Ja w wieku 15 lat miałem podobne problemy. I gdybym wtedy dostał AI w swoje ręce to też wolałbym porozmawiać z AI zamiast z rówieśnikami czy rodzicami. Ale to nie dlatego że AI jest takie świetne, tylko dlatego że byłem w szkole gnębiony a ro… ([link](https://www.youtube.com/watch?v=1j29IoHjf7c&lc=UgyF_xCXOtZuklWn4FN4AaABAg))

> Wręcz przeciwnie, ja ciągle słyszę narzekania na AI nie zawsze racjonalne. Przecież relacja z rówieśnikami często jest większym zagrożeniem od takiego AI. Mówmy o wszystkim, ale nie popadajmy w skrajności. AI przynajmniej nie szkaluje, nie poniża, nie wyśmiewa, nie znęca się itp. A rówieśnicy często są okrutni. ([link](https://www.youtube.com/watch?v=1j29IoHjf7c&lc=Ugxij6SP1DvufRXt1Y54AaABAg.AM-sOI_DM4OAO8GyAu1H0y))

</details>

### 14. AI progress pace: revolution or bubble? — *Tempo rozwoju AI: rewolucja czy bańka?*
Commenters debate the speed and trajectory of AI progress, with the dominant view being that AI is advancing extremely fast and will soon surpass humans in nearly everything, countered by a minority calling it hype or a speculative bubble.  
`argument_for` · `capabilities_hype` · 58 texts

- **Czy AI naprawdę rozwija się tak szybko, jak mówią firmy, czy to tylko nakręcany hype i bańka?** — Is AI really advancing as fast as companies claim, or is it just hype and a bubble? `capabilities_hype`
- **Czy za kilkanaście lat zostanie cokolwiek, w czym człowiek będzie lepszy od AI?** — In a decade or two, will there be anything humans are still better at than AI? `jobs_economy`
- ⚠️ **Jeśli AI przewyższy ludzi, czy będziemy w stanie ją kontrolować?** — If AI surpasses humans, will we be able to control it? `ai_safety_xrisk`

<details><summary>Representative quotes</summary>

> Game Over. To co jeszcze pół roku temu AI robiła słabo dziś robi niemal bezbłędnie. Rok temu myśl że AI zakoduje grę wzbudzała "taa, może za 5 lat" a tym czasem to już dzisiaj. Jak dojdą do tego roboty, a dojdą, nie widzę miejsca dla człowieka bo będzie pod każdym względem gorszy od AI i robotów. Z każdym miesiącem coraz trudniej mi wyobrazić sobie optymistyczną przyszłość. Praktycznie jedynie sztucznie wymuszone regulacje mogą uchronić ludzi przed utopią. ([link](https://www.youtube.com/watch?v=S4ORwO1h5Bk&lc=UgwRj6w8qckWv8NhnWp4AaABAg))

> nie ma i być może nigdy nie będzie AGI. Dzisiejsze prace nad AI polegają na zwiększaniu możliwości obliczeniowych, a dla AGI, dla uzyskania świadomości, nie wystarczy wziąć "większy młotek". Może się okazać że AI to największa bańka spekulacyjna wszechczasów. Już teraz instytucje finansujące badania, zaczynają przebąkiwać "a gdzie zwrot poniesionych nakładów" ... ([link](https://www.youtube.com/watch?v=V4VREmXMYDU&lc=UgwwDSNEZZ1Olz2OHpR4AaABAg.AP6nLLOE2zBAPd5HdEPMHV))

> Zastanawiam się, czy za 2-3 dekady będzie jakikolwiek zadanie, ktorego A.I. nie będzie umiało rozwiązać. Jeżeli tempo zmian w tej dziedzinie nie zachamuje to potrafię sobie wyobrazić, że nawet na polu wymagającym ogromnej kreatywności sieci neuronowe zostawią nas daleko w tyle. Nie wiem w czym ludzie będą mogli rywalizować wtedy z A.I.? ([link](https://www.youtube.com/watch?v=34QVkoJmBZw&lc=UgwG436fCp9z82faer94AaABAg.A3fERuIBnbGA3gk4qxcRAP))

> Piszesz o tym co jest teraz, gwarantuje Ci, że do 5 lat nie odróżnisz dzieła stworzonego przez AI od ludzkiego. To co napisałeś to coś w co chcemy wierzyć, ale jest już za późno, nie wypierajcie, przygotujcie się już dziś. Nie poznacie świata za 10 lat. ([link](https://www.youtube.com/watch?v=ri-fv-6FSxY&lc=UgwUSVxMyb_qsxXXCjl4AaABAg.A_Rvv9dmDABA_S2F95ExDR))

</details>

### 15. AI replacing doctors amid healthcare frustration — *AI zamiast lekarzy – frustracja służbą zdrowia*
Most commenters welcome AI in medicine as more accurate, up-to-date and accessible than Polish doctors and the NFZ system, often expressing contempt for doctors, while a minority insist on the human touch or dismiss 'AI will cure cancer' claims as hype or a cover for control.  
`argument_for` · `health` · 55 texts

- **Czy diagnoza z czatu AI jest bezpieczniejsza niż wizyta u lekarza i kiedy można jej ufać?** — Is a diagnosis from an AI chatbot safer than seeing a doctor, and when can it be trusted? `health`
- **Czy AI faktycznie pomogło już wynaleźć jakieś leki albo leczyć raka, czy to tylko marketing?** — Has AI actually helped discover drugs or treat cancer yet, or is that just marketing? `capabilities_hype`
- **Kto zadba o to, żeby AI w medycynie służyło pacjentom, a nie ubezpieczycielom i firmom farmaceutycznym?** — Who will ensure medical AI serves patients rather than insurers and pharma companies? `big_tech_power`

<details><summary>Representative quotes</summary>

> Sorry, ale porady lekarskie są obarczone większym ryzykiem błędu, np. w zestawianiu leków, niż porady AI. Takie marudzenie, jakby ludzie byli nieomylni, a tymczasem bredzą jak potłuczeni. Który lekarz, codziennie ran, do kawusi, czyta najnowsze badania naukowe z zakresu medycyny i nauk pokrewnych? Po prostu fizycznie jest to niemożliwe, a dla AI, to jest żaden problem. ([link](https://www.youtube.com/watch?v=ri-fv-6FSxY&lc=UgxKzXgCGYG2IVkO_FB4AaABAg))

> już teraz idę do lekarza z diagnozą popartą trzema róznymi czatami AI i jeszcze się nie pomyliłem... Zwykle lekarz sprowadza się do tego że tylko potwierdza i przepisuje mi leki. Pan ma rację , tylko wysokowyspecjalizowani lekarze będą się trzymać dbrze, ale też do czasu...Na dłuższą metę, roboty lekarze wyprą z czasem i tych najlepszych! Lekarz człowiek odejdzie do lamusa jak kiedyś kowale i kołodzieje... A za sto lat ludzie będą kręcili głowami z niedowierzania że jeszcze tak nie dawno operac… ([link](https://www.youtube.com/watch?v=eDt_C0U1i2o&lc=UgxrL4vu5-y2DmCdJLd4AaABAg))

> Mojego głupiego lekarza GP może zastąpić nawet bardzo słaby model AI... ([link](https://www.youtube.com/watch?v=eDt_C0U1i2o&lc=UgyOMJ8TAl-aIfY21BV4AaABAg))

> Dobrze, że tak jest, bo przy obecnej dostępności do specjalistów w publicznej służbie zdrowia w Polsce, AI "zdiagnozuje" nas o wiele szybciej. Wystarczy wrzucić wynik RTG czy USG i "diagnozę" mamy podaną na tacy :) ([link](https://www.youtube.com/watch?v=V4VREmXMYDU&lc=Ugwl9wAVALBgrVPiL454AaABAg))

</details>

## 3. Search questions (Google Trends)

_Not collected yet — the Trends collector is not built in this run._

## 4. Caveats

| source   |   collected |   kept_after_cleaning |   about_ai |   parents | from       | to         |
|:---------|------------:|----------------------:|-----------:|----------:|:-----------|:-----------|
| youtube  |       12415 |                 10468 |       6029 |        61 | 2024-01-18 | 2026-11-19 |

Cleaning outcomes: kept 10468, short 1726, not_polish 192, dup_exact 23, dup_near 6.

- **Sampling bias.** YouTube comments are drawn from videos YouTube's search ranks for our keywords, so they over-represent popular/sensational AI content and the people who comment on it. Comment order is YouTube's 'relevance', which favours liked comments. This is not a representative sample of Polish internet users, let alone of Poles.
- **Per-video concentration.** Commenters react to the specific video; check the '1 video' column before reading a theme as a general public concern.
- **Pipeline judgments.** AI-relevance (Claude Haiku), clustering (HDBSCAN; noise is excluded) and labels/questions (Claude Opus) are model outputs; spot-check quotes against links.
- **Anonymisation.** No author names are stored; @handles and URLs are stripped from text. Quotes are verbatim otherwise and links point to the public comment.
- **Sources skipped this run:** none. Not yet built: reddit, wykop, x (xAI), google trends, news-site comments. Facebook and TikTok are out of scope.
