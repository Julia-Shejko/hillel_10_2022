# <span style="color:violet">OOP. Abstract classes</span>


## <span style="color:purple">Materials</span>

- [YouTube](https://www.youtube.com/watch?v=Ej_02ICOIgs)
- [YouTube](https://www.youtube.com/watch?v=JeznW_7DlB0)
- [Abstract classes](https://www.geeksforgeeks.org/abstract-classes-in-python/)
- [@classmethod](https://www.tutorialsteacher.com/python/classmethod-decorator)
- [@staticmethod](https://www.tutorialsteacher.com/python/staticmethod-decorator)
- [@property](https://www.tutorialsteacher.com/python/property-decorator)
- [Descriptor](https://docs.python.org/3/howto/descriptor.html)


### Example with game units

```python
class BaseUnit: pass
class Unit(BaseUnit): pass
class BaseAttackProcess(ABC): pass

class AttackProcess(BaseAttackProcess):
    def __init__(self, unit: Unit) -> None:
        self._unit = unit

class Protection:
    def __init__(self) -> None:
        self.config = ""

class Damage:
    def __init__(self) -> None:
        self.config = ""

class DamageProcessor:
    def __init__(self, attacker: Unit, protector: Unit, protection: Protection, damage: Damage) -> None:
        self.attacker: Unit = attacker
        self.protector: Unit = protector
        self.protection = protection
        self.damage = protection

    def calculate(self):
        print("...")

class HealthProcessor:
    def __init__(self, unit, reduce_protocol) -> None:
        self.unit = unit
        self.reduce_protocol = reduce_protocol

    def reduce_health(self):
        self.reduce_protocol.calculate()
```

