Exception Handling Calculator 

[Armenian] Սա Python լեզվով գրված հրամանային տողի (CLI) հաշվիչ է, որի գլխավոր նպատակն է ցուցադրել Python-ում 
սխալների կառավարման (Exception Handling) և մուտքագրվող տվյալների վավերացման (validation) հիմնական գաղափարները:
Ծրագիրը պաշտպանված է օգտատիրոջ կողմից հնարավոր սխալ մուտքագրումներից և չի վթարվում (crash) անսպասելի տվյալներ ստանալիս:

[English] This is a command-line (CLI) calculator built with Python, designed primarily to demonstrate the 
concepts of Exception Handling and input validation. The program is fully protected against invalid user 
inputs and handles unexpected data gracefully without crashing.

Features

* **Թվերի անվտանգ մուտքագրում (Safe Number Input):**
  Ծրագիրը թույլ չի տալիս տեքստային նիշեր ներմուծել թվերի փոխարեն՝ կանխելով `ValueError` սխալը:
* **Գործողության վավերացում (Operation Validation):**
  Օգտագործվում է `try-except` բլոկ և արհեստական սխալի հարուցում (`raise ValueError`), որպեսզի թույլատրվեն
  միայն ճիշտ մաթեմատիկական նշանները (`+`, `-`, `*`, `/`):
* **Բաժանում զրոյի վրա (Zero Division Prevention):**
  Ծրագիրը որսում է զրոյի բաժանման փորձերը (`ZeroDivisionError`) և թույլ չի տալիս կատարել անթույլատրելի              գործողություն՝ խնդրելով նոր հայտարար ներմուծել:
* **Անխափան ցիկլեր (Infinite Input Loops):**
  Օգտատերը չի կարող շրջանցել սխալների ստուգումը. ծրագիրը կհարցնի նույն տվյալը այնքան ժամանակ, մինչև այն ճիշտ լինի:



Կոդի կառուցվածքը / Code Structure

Ծրագիրը բաժանված է 3 հիմնական ֆունկցիաների.
1. `number()` - Վավերացնում և վերադարձնում է իրական թվեր (floats):
2. `choice()` - Ստուգում է մաթեմատիկական նշանի ճշտությունը `try-except`-ով:
3. `result()` - Կատարում է հաշվարկը և կառավարում զրոյի բաժանման սխալը:
