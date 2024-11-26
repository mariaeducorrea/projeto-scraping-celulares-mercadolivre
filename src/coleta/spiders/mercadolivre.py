import scrapy




class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular#D[A:celular]"]
    page_count = 1
    max_pages = 10  #Definir o máximo de páginas a serem coletadas
    marca_lista = ["positivo", "multi", "infinix", "nokia", "zte", "samsung", "motorola", "lg", "huawei", "blu", "xiaomi", "asus", "redmi", "multilaser", "poco", "tcl", "apple", "alcatel", "semp", "red", "iphone","realme","redmagic","gradiente","oppo","agm","lenoxx","cat","honor"]






    def parse(self, response):
        
        #coleta página html e lista todos os elementos 'div' com a classe 'poly-card__content' - cada elemento é um produto na lista 
        produtos = response.css('div.poly-card__content')

        #loop para interar sobre todos os produtos encontrados
        for produto in produtos:

            # Coleta a lista produtos e faz nova lista com os elementos que possuem a classe 'poly-component__brand'
            marca = produto.css('span.poly-component__brand::text').get()

            if not marca:
                # Se a marca não foi encontrada diretamente, tenta inferir a marca a partir do nome
                nome = produto.css('h2.poly-box a::text').get()
                if nome:
                    # Divide o nome do produto em palavras
                    nome_split = nome.split()
                    # Itera sobre as palavras até encontrar uma válida (não na lista de excluídas)
                    for palavra in nome_split:
                        if palavra.lower() in self.marca_lista:
                            marca = palavra
                            break
                    


            #coleta a lista produtos e faz nova lista para cada produto em produtos com os elementos que possuem a classe 'poly-box a' 
            # valores = produto.css('div.poly-component__price span.andes-money-amount__fraction::text').getall()

            blocos = produto.css('div.poly-component__price')
            primeiro_bloco = blocos[0] if len(blocos) > 0 else None

             # Inicializar as variáveis aqui, antes de verificar os valores
            valor_antigo = None
            valor_atual = None
        

            if  primeiro_bloco:
                valores = primeiro_bloco.css('span.andes-money-amount__fraction::text').getall()

                if valores:
                    if len(valores) < 3:
                        valor_atual = valores[0]
                        valor_antigo = None
                 
                    if len(valores) > 2:
                        valor_antigo = valores[0]
                        valor_atual = valores[1]
                  
            

            yield {
                'página': self.page_count,
                'marca': marca,
                'nome': produto.css('h2.poly-box a::text').get(),
                'valor_antigo': valor_antigo,
                'valor_atual': valor_atual,
                'valor_antigo_cent': primeiro_bloco.css('s.andes-money-amount--previous span.andes-money-amount__cents::text').get(),
                'valor_atual_cent': primeiro_bloco.css('div.poly-price__current span.andes-money-amount__cents::text').get()
            }
        
        

        if self.page_count < self.max_pages: #verifica se a contagem de páginas é menor que o número máximo
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()  #busca especificamente o atributo href do link da próxima página
            if next_page:   #verifica se next_page contém uma URL válida
                self.page_count += 1    #Se próxima página existir o contador é incrementado em 1
                yield scrapy.Request(url=next_page, callback=self.parse)    

                #scrapy.Request - nova requisição para a URL da próxima página
                #callback=self.parse -  resposta dessa nova requisição deve ser processada pelo mesmo método parse

