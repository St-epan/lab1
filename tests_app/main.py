#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            rendered_page = render_main_page()  
            self.wfile.write(rendered_page.encode('utf-8'))  
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            rendered_page = render_about_page()  
            self.wfile.write(rendered_page.encode('utf-8'))
        elif self.path == '/contact':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            rendered_page = render_contact_page()  
            self.wfile.write(rendered_page.encode('utf-8'))
        elif self.path == '/services':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            rendered_page = render_services_page()  
            self.wfile.write(rendered_page.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def render_main_page():
    template = env.get_template('template.html')
    rendered_page = template.render(
        fish1_title="Золотистый карп",
        fish1_text="2000 р",
        fish2_title="Гуппи",
        fish2_text="500 р",
        fish3_title="Сом парчовый",
        fish3_text="1500 р",
    )
    return rendered_page

def render_about_page():
    template = env.get_template('about.html')
    rendered_page = template.render(
        fish1_title="Золотистый карп",
        fish1_text="Этот вид рыбы отличается яркой окраской и может достигать значительных размеров.",
        fish2_title="Гуппи",
        fish2_text="Небольшая и красочная рыба, популярная для домашнего аквариума.",
        fish3_title="Сом парчовый",
        fish3_text="Уникальный вид с характерными узорами на теле, высоко ценится среди аквариумистов.",
    )
    return rendered_page

def render_contact_page():
    template = env.get_template('contact.html')
    rendered_page = template.render(
        contact_email="contact@example.com",
        contact_phone="+7 (999) 999-99-99",
        contact_address="г. Москва, ул. Примерная, д. 1"
    )
    return rendered_page

def render_services_page():
    template = env.get_template('services.html')
    rendered_page = template.render(
        service1_title="Консультации",
        service1_description="Мы предоставляем экспертные консультации по уходу за аквариумами.",
        service2_title="Продажа рыбок",
        service2_description="У нас вы можете приобрести разные виды экзотических рыб.",
        service3_title="Обслуживание аквариумов",
        service3_description="Мы предлагаем услуги по обслуживанию аквариумов любой сложности."
    )
    return rendered_page

# Вызов функций для рендеринга страниц
render_main_page()
render_about_page()
render_contact_page()
render_services_page()

server = HTTPServer(('0.0.0.0', 8000), CustomHTTPRequestHandler)
print("Сервер запущен на http://0.0.0.0:8000")
server.serve_forever()