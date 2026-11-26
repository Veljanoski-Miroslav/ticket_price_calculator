# ticket_price_calculator

I filen price_calculator där utvecklaren har skrivit kod för åldern och pris för biljetterna så upptäckte jag ett fel med gränsvärden. Nämligen i kriterierna stod det att barn mellan 0-12 betalar 50kr/biljett och mellan 13-64år betalar 100kr/biljett. I koden hade utvecklaren angett 50 <= 13 som innebär att alla under och lika med 13 kommer att betala 50kr. Detta var inte det som angetts i kriterierna. 
Ett annat fel var i testkoden där utvecklaren inte hade lagt gränsvärderna som angivits i kriteriererna dvs 12,13,64. 
Dessa gärnsvärden behöver testas för att se om programmet fungerar vid gränsvärden. Jag har ändrat i testkoden och skrivit till i tabellen (12,50), (13,100), (64,100) för att se om testet går igenom. Numera finns det 15 godkända tester. 
