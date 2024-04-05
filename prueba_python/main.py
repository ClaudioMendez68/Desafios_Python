import template, names, images
from string import Template

# Captura de datos desde la API
imagenes = images.get_images('full')
espagnol = names.get_names('spanish')
ingles = names.get_names('english')

# Plantillas de reemplazo
img_template = Template('<img src=$url class="card-img-top" alt="...">')
lang_template = Template('<h5 class="card-title">$esp  -  $eng</h5>')
# Sustitución por plantillas
imagen = img_template.substitute(url = imagenes)
html_template = Template(template.html_temp)
html = html_template.substitute(body = imagen)
# Generación del texto HTML
text_body = ''
for i in range(len(imagenes)):    
    text_body += f'''
            <div class="col-sm-6">
                {img_template.substitute(url = imagenes[i])}
                <div class="card">
                    <div class="card-body">
                        {lang_template.substitute(esp = espagnol[i], eng = ingles[i])}
                    </div>
                </div>
            </div>
            '''
# Incorporación de texto HTML generado a plantilla general
html_template = Template(template.html_temp)
html = html_template.substitute(body = text_body)
# Generación de archivo .html
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html)