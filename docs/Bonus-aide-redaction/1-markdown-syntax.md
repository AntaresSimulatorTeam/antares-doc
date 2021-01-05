# Écrire en Markdown
# H1 `# H1`

## H2 `## H2`

### H3 `### H3`

## Text

|  text | Code  | Rendu  |
| ------------ | ------------ | ------------ |
|  italique | `*hello*`  | *hello*  |
|  gras | `**bonjour**`  | **bonjour**  |
|  lien |  ```[mon lien](https://google.com)``` |  [mon lien](https://google.com) |
| latex | `$$\sum^{N}_{i=0}{\Gamma_c}$$` | $$\sum^{N}_{i=0}{\Gamma_c}$$ |
|| `inline \\( \Gamma_c \\)` |inline \\(\Gamma_c\\) |


## Image
### Basic
```
![image](antares.png)
```

![image](antares.png)

### Specific size
```
![image](antares.png){: style="width: 200px; height: 200px"}
```
![image](antares.png){: style="width: 200px"}

### side by side
```
![image](antares.png)
![image](antares.png)
```
![image](antares.png){: style="width: 200px"}
![image](antares.png){: style="width: 200px"}

### Puces
```
* a
* b
* c
```

* a
* b
* c


### Code

```
 ```python
 def test(param: str = 'hello'):
     return str + 'a'
 ```
```

```python
def test(param: str = 'hello'):
    return str + 'a'

```


### Table

| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

```
| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |
```
