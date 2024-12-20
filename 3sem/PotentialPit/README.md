# Моделирование - Потенциальная яма

## Теория
### Текст задания

### Решение

**Реализация:**

[**Дискретизируем**](#) пространство на x ∈ [–L/2; L/2]:

```math
x_i = -\frac{L}{2} + i \Delta x; \quad i = 0, 1, \ldots, N; \quad \Delta x = \frac{L}{N}.
```

[**Дискретизируем**](#) оператор H с использованием конечных разностей:

_**Кинетический** (3-х диагональная матрица):_

```math
T = -\frac{\hbar^2}{2m} \nabla^2
```

```math
\frac{d^2 \Psi(x)}{dx^2} = \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{\Delta x^2}
```

```math
T \psi_i = -\frac{\hbar^2}{2m} \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{\Delta x^2}
```

```math
T_{i,i} = \frac{\hbar^2}{m \Delta x^2}
```

```math
T_{i,i-1} = T_{i,i+1} = -\frac{\hbar^2}{2m \Delta x^2}
```

_**Потенциальный** (диагональная матрица):_

```math
V_{i,i} = V(x_i)
```

Итоговый гамильтониан:

```math
H = T + V
```

```math
H_{i,i} = \frac{\hbar^2}{m \Delta x^2} + V(x_i) \quad \text{— значения на диагонали}
```

```math
H_{i,i-1} = H_{i,i+1} = -\frac{\hbar^2}{2m \Delta x^2} \quad \text{— элементы соседних строк}
```

Нормировка с учетом шага $\Delta x$:

```math
\psi_i = \frac{\psi_i}{\sqrt{\Delta x}}
```

## Установка

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```
