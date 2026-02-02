# Modellering og Simulation 

## Faglige mål 
- Forstå inheritance og Polymorfi
    - Recap: inheritance
- Abstract classes og metoder
    - Polymorfi
    - DRY (Don't Repeat Yourself) principle
- Configuration dictionaries
    - unpacking dictionaries 
- List comprehensions (recap)
- Data Visualization
    - Matplotlib Animation
- Agent Based Modelling (ABM)  
- Videnskabsteori
    - Naturvidenskabelig metode
        - Labtoratorie- og felteksperiment
        - Modeller 
        - Hypotetisk-deduktive metode



## Materialer
- [Emprisk og formel](https://vidensmoenstre.systime.dk/?id=129)
- [Deduktion og induktion](https://vidensmoenstre.systime.dk/?id=143)

## Further reading 
- [Agent based modelling (ABM)](https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/epstein_axtell.pdf)
- [Game Theory by ABM](https://math.libretexts.org/Bookshelves/Applied_Mathematics/Agent-Based_Evolutionary_Game_Dynamics_(Izquierdo_Izquierdo_and_Sandholm)/02%3A_Our_first_agent-based_evolutionary_model/2.01%3A_Our_very_first_model)



## Abstract Klasser og Polymorfi

- Læs https://docs.python.org/3/library/abc.html
- Læs https://www.geeksforgeeks.org/python/polymorphism-in-python/


- Forklar begreber 
    - Nedarvning
    - Polymorphism 
- forklare hvad en abstract class er, og hvorfor man bruger abc

    *The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system". The principle has been formulated by Andy Hunt and Dave Thomas in their book The Pragmatic Programmer. They apply it quite broadly to include database schemas, test plans, the build system, even documentation.When the DRY principle is applied successfully, a modification of any single element of a system does not require a change in other logically unrelated elements. Additionally, elements that are logically related all change predictably and uniformly, and are thus kept in sync.(wikipedia)*

- implementere egne klasser, der overholder et fælles interface

- anvende **kwargs og dictionary-unpacking i constructors


### Do it yourself

- Læs artiklen https://realpython.com/instance-class-and-static-methods-demystified/
- Implementer klasser `Rectangle` og `Circle` i filen models/Shape.py
    - **Inheritance**: `Circle` skal nedarve fra `Shape`
    - **Constructor (__init__)**
        - Circle skal bruge **kwargs som input
        - Circle skal gemme radius som et attribut
    - **abstractmetod**: Implementér metoden area(), der skal returnere cirklens areal.
    - **classmetode**: Implementér metoden from_config(cls, config), der skal 
        - modtage en dictionary
        - validere input
        - oprette og returnere et Circle-objekt
    - **staticmetode** Implementér static metode validate_config(config) der skal:
        - sikre at "radius" findes i dictionary
        - sikre at radius er et positivt tal
        - Hvis input er forkert, skal der raises en ValueError



## Agent Based Modelling
:raising_hand: _Hvad er ABM?_

- Læs artiklen om agent based modelling https://math.libretexts.org/Bookshelves/Applied_Mathematics/Agent-Based_Evolutionary_Game_Dynamics_(Izquierdo_Izquierdo_and_Sandholm)/01%3A_Introduction/1.02%3A_Introduction_to_agent-based_modeling
- En video on net-logo og ABM https://www.youtube.com/watch?v=ocp3OdOvrZM
- Net-logo: https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Sample%20Models/Biology/Virus.nlogox

## Bygge Simulationsmodellen 
- Læs artiklen om prey og predator model https://rf.mokslasplius.lt/agent-based-prey-predator-model/

### Regler
:raising_hand: _Hvilke regler skal modellen have?_

### Klasse Agent
- Implementere klasse `Agent`som en abstract class
- Diskussion:
    - Hvilke metoder kunne en agent have?

### Klasse Prey
- Implementere klasser `Prey` og `Predator`, ved at implementere abstrakt klasse `Agent`. 
    - :raising_hand: Hvilke attribute skal en `Prey` have?
    - Implementere de abstrakte metoder af `Agent`
        - **move**
        - **eat**
        - **reproduce**
    - :raising_hand: Hvordan teste man metoderne?

### Klasse Predator
- Komplet Klasse `Pedator` ved at implementere de abstrakte klasse `Agent`.
- :raising_hand: Er der noget flere attributer eller metoder `Predator` skal have? 




### Simulerings Engine

- Simuleringsløkke: for hvert tidskridt 
    - Bevægelse
    - Interaktioner (Spise, jage)
    - Reproduktion
    - Fjern døde
    - Registrer statistik

## Do it yourself

I skal færdiggøre en lille Agent Based Model med
 - en toroidal 2D verden (wrap-around)
 - en phase-based simulationsmotor:
 1. move
 2. interact
 3. reproduce
 4. cleanup (dead)

I får en fil med: 
- `ToroidalPosition` 
- `Agent` med `move()`, `interact`, `reproduce()` som abstract methods
- `Model` med `step()` der kører faserne
- `Prey` og `Predator` med TODO

**I må ikke ændre engine-strukturen**. I skal implementere de manglende metoder.

### Opgave 1
- Regler
    - Prey/Predator skal flytte sig i et random 4-nabolag(op/ned/venstre/højre)
    - Prey/Predator mister energi hver tur self.energy -= 1 
    - self.die() hvis energy <= 0
- Implementér:
    - Prey.move()
    - Predator.move()

- Test
    - print af antal prey/predator pr.step


### Opgave 2
- Regler:
    - Predator skal kunne spise én prey hvis der står en prey på samme celler.
    - Når prey spises:
        - prey dør (prey.die())
        - predator får energi (fx +10)
- Implementér:
    - Predator.interact()
        - finde prey på samme celle (`model.agent_at()`)
        - prey.die() hvis er blevet spist
- hint

```python
agents_here = self.model.agents_at(self.position)
prey_at_position = [a for a in agents_here if isinstance(a, Prey)]
```

### Opgave 3

- Regler
    - Hvis prey/predator har høj energi, eller efter en reproduce_rate, laver den en ny baby.
    - Baby spawn'er ved samme position (eller nabo, hvis i vil)
    - Forælderen mister energi (fx halverer sin energi)
- Implementér
    - Prey.reproduce()
    - Predator.reproduce()

- hint 
```python         
    baby = self.__class__(self.model,
                        uid=self.model.next_uid(),
                        position=self.position,
                        energy=10)
    self.model.add_agent(baby)
    self.energy//=2 
```

### Opgave 4 -- Test 

1. Sikre at `position` altid ligger indenfor Toroidal world 
    - Skriv en lille test i i den samme fil eller lav en ny fil: 

    ```python
    def test_toroidal_wrap():
        model = Model(width=10, height=6, seed=1)
        WorldPrey, _ = make_world_classes(model)
        p = WorldPrey(model, uid=0, position=(9,5))
        p.move_by(1,0)
        assert p.position == (0,5)
    ```
2. Test at døde agents fjernes korrekt.

    ```python
    def test_agent_dies():
        model = Model(5,5,seed=1)
        WorldPrey, _ = make_world_classes(model)

        p = WorldPrey(model, uid=0, energy=1)
        model.step()
        assert len(model.agents) == 0
    ```
3. Test interaktion mellem agents (predator spiser prey)

    ```python
    TODO
    assert prey not in model.agents
    assert predator.energy >10
    ```

### Opgave 5 -- Datasamling og statisk plot

1. Gem data over tid
    - antal prey og predator efter hver step
2. Plot populationer over tid

### Animation med matplotlib

1. animer population over tid 
2. (optional) Animer 2D-verdenen. 




