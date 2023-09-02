
# Memento
class Memento:
    def __init__(self, state):
        self._state = state
    
    @property
    def state(self):
        return self._state


# Originator
class TextArea:
        
    def __init__(self, value = ""):
        self._value = value
    
    def save(self):
        return Memento(self._value)
    
    def restore(self, memento: Memento):
        self._value = memento.state
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    

# CareTaker
class Editor:
    def __init__(self, originator: TextArea):
        self._originator = originator
        self._history = []
    
    def write(self, text: str):
        self._originator.value = text
        self._history.append(self._originator.save())
        
    def undo(self):
        self._originator.restore(self._history.pop())
    
    @property
    def current_value(self):
        if self._history:
            return self._history[-1].state
        return ""


if __name__ == "__main__":
    textarea = TextArea()
    editor = Editor(textarea)
    editor.write("Hello World")
    print(editor.current_value)
    editor.write("What's up with you?")
    print(editor.current_value)
    editor.write("Maybe something new")
    print(editor.current_value)
    editor.undo()
    print(editor.current_value)
    editor.undo()
    print(editor.current_value)
    editor.undo()
    print(editor.current_value)