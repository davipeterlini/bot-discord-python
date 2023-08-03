# bot-discord-python
Create a Bot in python for conect in Discord

# Video
* [Crie um bot no Discord com Python - Hospedagem gratuita na nuvem](https://www.youtube.com/watch?v=WdlJi5j4pps)

## 1 - Configurando o bot no Discord
* Crie um servidor novo no Discord ou tenha acesso de admin no servidor desejado 
    * [Exemplo de Servidor](https://discord.com/channels/1136788876225163274)
* Area do discord para dev
    * [Discord Dev](https://discord.com/developers/applications) --> New Application --> Nome (Aceite os termos) --> Create --> Click em Bot --> Troque o Nome --> Click em Reset Token --> Copie o Valor para local seguro  --> Habilite o: *Message Content Intent*

# 2 - Instalação do bot no servidor do Discord
* Click em OAuth2 --> Copie o ClientId para um local seguro --> [Acesse a url]( https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=CLIENT_ID) --> no lugar de CLIENT_ID coloque o valor do ClientId do passo anterior --> Selecione o servidor --> Autorizar --> Check de Não Robo --> Verificar se o bot esta ativo no Discord --> [Exemplo de Servidor com Bot Ativo](https://discord.com/channels/1136788876225163274)


# 3 - Utilizando o Repl.it - IDE na nuvem de Python
* [replit](https://replit.com/) --> Create Repl --> Escolha: Python --> Nome --> Create Repl --> no arquivo main cole as linhas abaixo: 
    ```shell script
    import discord 
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='/', intents=intents)
    ```

# 4 - Adicionando o token de acesso no Repl.it
* Use a ferramenta Secrets do Replit --> New Secret --> Key: *DISCORD_TOKEN* --> Value: Cole o token do discord dev
* Adicione as linhas abaixo: 
    ```shell script
    import os

    my_secret = os.environ['DISCORD_TOKEN']

    bot.run(my_secret)
    ```

# 5 - Colocando o bot para rodar
* Adicione as linhas abaixo antes do *bot.run* 
    ```shell script
    @bot.command()
    async def inverse(ctx, message):
    await ctx.send(message[::-1])
    ```
* Realize o teste do Bot no servidor em que foi adicionado, no canal digite: 
    ```shell script
    /inverse STRING
    ```
** ao fechar o navegador o bot é desligado por isso siga para o último passo

# 6 - Hospedagem gratuita do bot na nuvem do Uptime Robot 
* Crie um servidor no replit atraves da criação do arquivo com nome: *keep_alive.py* e coloque as linhas abaixo: 
    ```shell script
    from flask import Flask
    from threading import Thread

    app = Flask('')

    @app.route('/')
    def home():
        return "I'm alive"

    def run():
    app.run(host='0.0.0.0',port=8080)

    def keep_alive():
        t = Thread(target=run)
        t.start()
    ```

* Adicione o servidor no Bot
    * No arquivo *main.py* adicione o servidor através das linhas abaixo
        ```shell script
        from keep_alive import keep_alive

        keep_alive()
        bot.run(my_secret)
        ```
    * Execute o replit
        * No lado direito da tela sera exibido o valor da URL do Servidor

    #### Isso faz com que o arquivo fique ativo no servidor por apenas 1 hora 


* Para que fique ativo gratuitamente por tempo indeterminado basta usar o [uptimerobot](https://uptimerobot.com/)
    * Crie uma conta, caso ainda nao possua
    * Crie um monitor --> Add New Monitor --> Monitor Type: HTTP(s) --> Escolha um Friendly Name --> Cole a URL do Servidor gerado acima

# 7 - Conclusão
[Documentação Completa do Replit ](https://docs.replit.com/tutorials/python/build-basic-discord-bot-python)