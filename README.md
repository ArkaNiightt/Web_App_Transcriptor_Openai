<p align="center">
    <img src="images/image_logo_project.gif" align="center" width="10%">
</p>
<p align="center"><h1 align="center">WEB_APP_TRANSCRIPTOR_OPENAI</h1></p>
<p align="center">
 <em>Transcrevendo a Web, um Sussurro de Cada Vez!</em>
</p>
<p align="center">
 <img src="https://img.shields.io/github/license/ArkaNiightt/Web_App_Transcriptor_Openai?style=default&logo=opensourceinitiative&logoColor=white&color=00ff86" alt="licença">
 <img src="https://img.shields.io/github/last-commit/ArkaNiightt/Web_App_Transcriptor_Openai?style=default&logo=git&logoColor=white&color=00ff86" alt="último commit">
 <img src="https://img.shields.io/github/languages/top/ArkaNiightt/Web_App_Transcriptor_Openai?style=default&color=00ff86" alt="linguagem principal do repositório">
 <img src="https://img.shields.io/github/languages/count/ArkaNiightt/Web_App_Transcriptor_Openai?style=default&color=00ff86" alt="número de linguagens no repositório">
</p>
<p align="center"><!-- opção padrão, sem badges de dependência. -->
</p>
<p align="center">
 <!-- opção padrão, sem badges de dependência. -->
</p>
<br>

## 🔗 Índice

- [📍 Visão Geral](#-visão-geral)
- [👾 Funcionalidades](#-funcionalidades)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
  - [📂 Índice do Projeto](#-índice-do-projeto)
- [🚀 Começando](#-começando)
  - [☑️ Pré-requisitos](#-pré-requisitos)
  - [⚙️ Instalação](#️-instalação)
  - [🤖 Uso](#-uso)
  - [🧪 Testes](#-testes)
- [📌 Roteiro do Projeto](#-roteiro-do-projeto)
- [🔰 Contribuindo](#-contribuindo)
- [🎗 Licença](#-licença)
- [🙌 Agradecimentos](#-agradecimentos)

---

## 📍 Visão Geral

O projeto WebAppTranscriptorOpenai é uma ferramenta inovadora projetada para converter linguagem falada em texto escrito. Ele utiliza o sistema Whisper ASR da OpenAI para transcrever áudio de várias fontes, incluindo microfones e arquivos de vídeo. Esta aplicação amigável, com recursos de comunicação em tempo real e tratamento de erros, é ideal para profissionais que precisam de transcrições rápidas e precisas, como jornalistas, pesquisadores e estudantes.

---

## 👾 Funcionalidades

|      | Funcionalidade      | Resumo       |
| :--- | :---:               | :---         |
| ⚙️  | **Arquitetura**     | <ul><li>O projeto é estruturado em dois arquivos Python principais: `app.py` e `utils.py`.</li><li>`app.py` serve como ponto de entrada principal, fornecendo a interface do usuário e lidando com as interações do usuário.</li><li>`utils.py` gerencia operações de arquivos de áudio e vídeo, incluindo extração de áudio de arquivos de vídeo e transcrição do conteúdo de áudio usando o sistema Whisper ASR da OpenAI.</li></ul> |
| 🔩 | **Qualidade do Código** | <ul><li>O código é bem estruturado e modular, com clara separação de responsabilidades entre `app.py` e `utils.py`.</li><li>Há tratamento eficaz de erros e notificações de sucesso para interações do usuário.</li><li>O código utiliza recursos modernos do Python e bibliotecas, como Streamlit para a interface do usuário e OpenAI para o serviço de transcrição.</li></ul> |
| 📄 | **Documentação**     | <ul><li>A linguagem principal usada no projeto é Python, com um total de 2 arquivos Python e 2 arquivos de texto.</li><li>O projeto usa `pip` como gerenciador de pacotes, com dependências especificadas em `requirements.txt`.</li><li>Instruções de instalação e uso são fornecidas, incluindo comandos para instalar dependências e executar a aplicação.</li></ul> |
| 🔌 | **Integrações**      | <ul><li>O projeto integra-se com o sistema Whisper ASR da OpenAI para serviços de transcrição.</li><li>Utiliza a biblioteca Streamlit para a interface do usuário e WebRTC para comunicação em tempo real.</li><li>O projeto também integra o framework multimídia `ffmpeg` para manusear vídeo, áudio e outros arquivos e fluxos multimídia.</li></ul> |
| 🧩 | **Modularidade**     | <ul><li>O projeto é modular, com módulos Python separados para diferentes funcionalidades (`app.py` e `utils.py`).</li><li>Cada módulo tem um papel específico, tornando o código fácil de entender e manter.</li></ul> |
| 🧪 | **Testes**           | <ul><li>Embora não haja arquivos de teste explícitos no projeto, as instruções de uso incluem um comando para executar testes com `pytest`.</li><li>Isso sugere que o projeto pode ter um framework de testes configurado, embora os detalhes não sejam especificados no contexto fornecido.</li></ul> |
| ⚡️  | **Desempenho**      | <ul><li>O projeto utiliza bibliotecas eficientes como `numpy` e `pandas` para manipulação de dados, conhecidas por seu desempenho.</li><li>O uso do sistema Whisper ASR da OpenAI para transcrição provavelmente garante alta precisão e velocidade.</li></ul> |
| 🛡️ | **Segurança**       | <ul><li>O projeto estabelece uma conexão segura com o cliente OpenAI usando uma chave de API.</li><li>No entanto, sem mais informações, é difícil avaliar completamente as medidas de segurança do projeto.</li></ul> |

---

## 📁 Estrutura do Projeto

```sh
└── Web_App_Transcriptor_Openai/
    ├── app.py
    ├── ffmpeg.exe
    ├── packages.txt
    ├── requirements.txt
    └── utils.py
```

### 📂 Índice do Projeto

<details open>
 <summary><b><code>WEB_APP_TRANSCRIPTOR_OPENAI/</code></b></summary>
 <details>
  <summary><b>__root__</b></summary>
  <blockquote>
   <table>
   <tr>
    <td><b><a href='https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/blob/master/utils.py'>utils.py</a></b></td>
    <td>- O módulo 'utils.py' no projeto gerencia principalmente operações de arquivos de áudio e vídeo<br>- Extrai áudio de arquivos de vídeo, salva-os temporariamente e transcreve o conteúdo de áudio usando o sistema Whisper ASR da OpenAI<br>- Este módulo também estabelece uma conexão com o cliente OpenAI usando uma chave de API, garantindo integração perfeita com os serviços da OpenAI.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/blob/master/app.py'>app.py</a></b></td>
    <td>- O 'app.py' serve como o ponto de entrada principal para a ferramenta de transcrição de áudio<br>- Fornece três métodos de transcrição: via microfone, vídeo ou arquivo de áudio<br>- A ferramenta usa a biblioteca Streamlit para a interface do usuário, WebRTC para comunicação em tempo real e OpenAI para o serviço de transcrição<br>- Também inclui tratamento de erros e notificações de sucesso para interações do usuário.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/blob/master/requirements.txt'>requirements.txt</a></b></td>
    <td>- O arquivo 'requirements.txt' especifica os pacotes Python necessários para o projeto<br>- Garante ambientes consistentes em diferentes configurações, auxiliando na reprodutibilidade do projeto<br>- Os pacotes listados variam de manipulação de dados (pandas, numpy), frameworks web (streamlit), a bibliotecas de machine learning (openai), indicando um escopo de aplicação diversificado.</td>
   </tr>
   <tr>
    <td><b><a href='https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/blob/master/packages.txt'>packages.txt</a></b></td>
    <td>- O 'packages.txt' serve como um manifesto para o projeto, especificando as dependências externas necessárias para o software funcionar corretamente<br>- Neste caso, indica a necessidade do pacote ffmpeg, um poderoso framework multimídia usado para manipular vídeo, áudio e outros arquivos e fluxos multimídia dentro do código do projeto.</td>
   </tr>
   </table>
  </blockquote>
 </details>
</details>

---

## 🚀 Começando

### ☑️ Pré-requisitos

Antes de começar com o Web_App_Transcriptor_Openai, certifique-se de que seu ambiente de execução atenda aos seguintes requisitos:

- **Linguagem de Programação:** Python
- **Gerenciador de Pacotes:** Pip

### ⚙️ Instalação

Instale o Web_App_Transcriptor_Openai usando um dos seguintes métodos:

**Compilação a partir do código-fonte:**

1. Clone o repositório Web_App_Transcriptor_Openai:

```sh
❯ git clone https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai
```

2. Navegue até o diretório do projeto:

```sh
❯ cd Web_App_Transcriptor_Openai
```

3. Instale as dependências do projeto:

**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

### 🤖 Uso

Execute o Web_App_Transcriptor_Openai usando o seguinte comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {ponto_de_entrada}
```

### 🧪 Testes

Execute o conjunto de testes usando o seguinte comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

---

## 📌 Roteiro do Projeto

- [X] **`Tarefa 1`**: <strike>Implementar a funcionalidade um.</strike>
- [ ] **`Tarefa 2`**: Implementar a funcionalidade dois.
- [ ] **`Tarefa 3`**: Implementar a funcionalidade três.

---

## 🔰 Contribuindo

- **💬 [Participe das Discussões](https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/discussions)**: Compartilhe seus insights, forneça feedback ou faça perguntas.
- **🐛 [Reporte Problemas](https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/issues)**: Envie bugs encontrados ou registre solicitações de recursos para o projeto `Web_App_Transcriptor_Openai`.
- **💡 [Envie Pull Requests](https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai/blob/main/CONTRIBUTING.md)**: Revise PRs abertos e envie seus próprios PRs.

<details closed>
<summary>Diretrizes de Contribuição</summary>

1. **Faça um Fork do Repositório**: Comece fazendo um fork do repositório do projeto para sua conta do GitHub.
2. **Clone Localmente**: Clone o repositório forkado para sua máquina local usando um cliente git.

   ```sh
   git clone https://github.com/ArkaNiightt/Web_App_Transcriptor_Openai
   ```

3. **Crie um Novo Branch**: Sempre trabalhe em um novo branch, dando-lhe um nome descritivo.

   ```sh
   git checkout -b nova-funcionalidade-x
   ```

4. **Faça Suas Alterações**: Desenvolva e teste suas alterações localmente.
5. **Commite Suas Alterações**: Faça commit com uma mensagem clara descrevendo suas atualizações.

   ```sh
   git commit -m 'Implementada nova funcionalidade x.'
   ```

6. **Envie para o GitHub**: Envie as alterações para o seu repositório forkado.

   ```sh
   git push origin nova-funcionalidade-x
   ```

7. **Envie um Pull Request**: Crie um PR contra o repositório original do projeto. Descreva claramente as alterações e suas motivações.
8. **Revisão**: Uma vez que seu PR for revisado e aprovado, ele será mesclado ao branch principal. Parabéns pela sua contribuição!

</details>

<details open>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com{/ArkaNiightt/Web_App_Transcriptor_Openai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ArkaNiightt/Web_App_Transcriptor_Openai">
   </a>
</p>
</details>

---
