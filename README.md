# python-runtime-function-creation
create functions in python dynamically during runtime


#### a little overview about this repo

While working on a project, I stumbled upon the idea of creating functions and variables dynamically during runtime. I realized that this approach is already used by many, but it was a new discovery for me! 😄

- in python we can create variables in runtime using globals() or locals() depending on desired context
    - for ex.
```python
globals()["some_var_name"] = "its dynamic value" ## get it all from user or a certain condition depends on the needs
```
- By combining globals()/locals() with exec() and eval(), you can create a complete runtime code creation system. However, a word of caution: this method can introduce security vulnerabilities if not implemented carefully.
- Runtime code execution is inherently dangerous. Using exec() and eval() with user-provided inputs can expose your code to code injection attacks. Always sanitize input and follow best security practices when implementing any form of dynamic code execution in your projects, especially in public-facing applications.
