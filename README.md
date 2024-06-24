# README.txt

## Restricciones de Acceso Implementadas

### 1. Restricción por Autenticación

- **Vista:** `welcome`
- **Descripción:** Esta vista muestra la página de bienvenida y sólo es accesible para usuarios que han iniciado sesión.
- **Implementación:**

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def welcome(request):
    return render(request, 'welcome.html')
```

### 2. Restricción por Edad
- **Vista:** `restricted_view` 
- **Descripción:** Sólo es accesible para usuarios mayores de 18 años. Esta restricción se implementa utilizando el decorador `user_passes_test` y la función `es_adulto`.
- **Implementación:**

```python
from django.contrib.auth.decorators import user_passes_test

def es_adulto(user):
    try:
        miembro = Miembros.objects.get(user=user)
        return miembro.edad >= 18
    except Miembros.DoesNotExist:
        return False

@user_passes_test(es_adulto)
def restricted_view(request):
    return render(request, 'restricted.html')
