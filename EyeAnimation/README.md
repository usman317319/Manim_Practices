
<h1>Example</h1>
<img src ='./Example.gif'>

<h1>Usage<h1>


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
