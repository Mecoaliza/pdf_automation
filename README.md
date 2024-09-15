# Conversão de PDFs em imagens JPG

    -  Regras de négocio:
        1. A automação foi feita a partir da necessidade de padronizar a qualidade da imagens que estavam sendo salvas.
        2. Em um arquivo pdf pode vir mais de um cartão assinado, e todos devem ser salvos para a importação no sistema. Dessa forma foi usada a lógica de salvar os arquivos: AA, AB, AC, etc.
        3. No fim do script foi usado o Tkinter, pois essa automação faz parte de um projeto que depende de mensagens vizuais 
        para prosseguir para a proxima etapa. 

- Todos os arquivos PDF que estão em uma pasta específica (pdf_folder) são verificados e cada página desses PDFs são convertidas em uma imagem no formato JPG.

- A conversão é feita usando a biblioteca pdf2image, que transforma cada página de um PDF em uma imagem.

### Controle de nomes de arquivos:

 - Todas as imagens são salvas com o prefixo AA.
 - Se o pdf tive mais de uma página, então o arquivo é salvo com o mesmo nome é prefixo AB, AC e assim sucessivamente.

### Salvamento das imagens:

- As imagens de cada página do PDF são salvas em uma pasta de saída (save_folder), em formato JPG, com qualidade máxima (100).

### Exibição de uma mensagem de conclusão

- Após a conversão de todos os PDFs, o código exibe uma caixa de diálogo utilizando o Tkinter, informando que o processo foi concluído com sucesso.