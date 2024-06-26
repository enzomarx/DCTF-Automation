# DCTF Automation

Este projeto automatiza a transmissão de DCTF para várias empresas utilizando o Domínio Web Thomson Reuters e o app da Receita DCTF. A automação é realizada utilizando `pyautogui` para simular interações com a interface do usuário e `tkinter` para criar uma interface gráfica para o usuário.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/dctf_automation.git
    cd dctf_automation
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

## Uso

1. Execute a interface gráfica do usuário:
    ```bash
    python src/gui.py
    ```

2. Insira os dados necessários (CNPJ e período) e clique em "Iniciar" para iniciar a automação.

## Dependências

- `pyautogui`: Biblioteca para automação da interação com a interface do usuário.
- `tkinter`: Biblioteca para criação de interfaces gráficas.
- `time`: Biblioteca padrão do Python para controle de tempo.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
x'