# Create Gif
Transforma um grupo de imagens em um gif usando a biblioteca [**imageio**](https://imageio.readthedocs.io/en/stable/index.html).

## Como funciona
Execute o script pelo terminal passando também o caminho até as imagens no qual quer transformar em gif.

```shell
python /path/to/script.py '/path/to/images'
```

Para funcionar, as imagens precisam estar nomeadas de maneira específica para poder determinar a ordem no gif.  
Ex: **\<frame>\<extensão> (1.png, 2.png, 3.jpg, 4.jpg)**  
 - *Válido apenas as extensões: .png e .jpg*
```
images
├── 1.png
├── 2.png
├── 3.png
├── 4.png
├── 5.png
└── 6.png
```

Não importa se ter algum arquivo aleatório no meio, pois irá pegar apenas os arquivos válidos.
```
images
├── 1.jpg
├── 2.jpg
├── 3.jpg
├── 4.jpg
├── outro_arquivo.txt
└── filme_aleatório.mp4
```