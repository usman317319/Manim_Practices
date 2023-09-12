
# Example
<img src ='./Example.gif'>

# Usage

```python
class Example(Scene):
    def construct(self):     
        r = Rectangle()
        self.wait()
        self.play(OpeningEye(r))
        self.wait()
        self.play(ClossingEye(r))
        self.wait() 
```

