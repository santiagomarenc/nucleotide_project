### 🧪 Casos de prueba manuales

| Entrada        | Resultado esperado                  |
|---------------|-------------------------------------|
| "ATGC"        | A=1, T=1, G=1, C=1, longitud=4      |
| "aaaa"        | A=4, longitud=4                     |
| " at gc "     | A=1, T=1, G=1, C=1, longitud=4      |
| ""            | longitud=0                          |

### ✅ Resultados (completa al correr el programa)

- Caso 1 ("ATGC"):
  - Obtuve: 
sequence: ATGC
a_content: 1   c_content: 1   t_content: 1   g_content: 1
Length: 4

  - ¿Coincide? Sí 

- Caso 2 ("aaaa"):
  - Obtuve: 
sequence: AAAA
a_content: 4   c_content: 0   t_content: 0   g_content: 0
Length: 4

  - ¿Coincide? Sí 

- Caso 3 (" at gc "):
  - Obtuve:
sequence: ATGC
a_content: 1   c_content: 1   t_content: 1   g_content: 1
Length: 4

  - ¿Coincide? Sí

- Caso 4 (""):
  - Obtuve:
error: no sequence found, length: 0

  - ¿Coincide? Sí 