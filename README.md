# GeoLabeler
Esta aplicação é uma ferramenta de anotação de imagens que permite ao usuário selecionar regiões de interesse em uma imagem e classificá-las em diferentes categorias e subcategorias. As anotações são salvas em um arquivo CSV para posterior análise.

## Funcionalidades

- Carregar uma imagem para anotação.
- Selecionar regiões retangulares na imagem.
- Classificar as regiões selecionadas em categorias e subcategorias.
- Salvar as anotações em um arquivo CSV.
- Interface gráfica amigável utilizando Tkinter e Matplotlib.

## Requisitos

- Python 3.x
- Bibliotecas listadas no arquivo [`requirements.txt`]

## Instruções para Rodar a Aplicação

### Passo 1: Criar um Ambiente Virtual

Para isolar as dependências da aplicação, é recomendado criar um ambiente virtual. Abra o terminal e execute o seguinte comando:

```bash
python -m venv venv
```

### Passo 2: Ativar o Ambiente Virtual

Ative o ambiente virtual criado no passo anterior. O comando para ativar o ambiente virtual varia conforme o sistema operacional:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS e Linux:**

  ```bash
  source venv/bin/activate
  ```

### Passo 3: Instalar Dependências

Com o ambiente virtual ativado, instale as dependências necessárias para rodar a aplicação. Execute o seguinte comando:

```bash
pip install -r requirements.txt
```

### Passo 4: Executar a Aplicação

Após instalar as dependências, execute o arquivo [`main.py`]

```bash
python main.py
```

## Uso da Aplicação

1. **Seleção de Imagem:** Ao iniciar a aplicação, uma janela de diálogo será aberta para que você selecione um arquivo de imagem (formatos suportados: `.tif`, `.jpg`, `.png`).

2. **Seleção do Local de Salvamento:** Após selecionar a imagem, outra janela de diálogo será aberta para que você escolha o local onde deseja salvar o arquivo CSV com as anotações.

3. **Anotação da Imagem:** A imagem selecionada será exibida em uma janela. Utilize o mouse para desenhar retângulos nas regiões de interesse. Selecione a categoria e subcategoria apropriadas para cada região.

4. **Salvar Anotações:** Após concluir as anotações, clique no botão "Salvar e sair" para salvar as anotações no arquivo CSV e fechar a aplicação.

## Adicionando Novas Labels

Para adicionar novas categorias e subcategorias, edite o arquivo [`config.py`]

Você pode adicionar novas categorias ou subcategorias conforme necessário.

## Contato

Para mais informações ou dúvidas, entre em contato com o desenvolvedor da aplicação.

---

Este documento fornece uma visão geral da aplicação, bem como instruções detalhadas para instalação e uso. Siga os passos cuidadosamente para garantir que a aplicação funcione corretamente.
