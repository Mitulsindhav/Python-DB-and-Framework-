from django.template import Template, Context
from django.conf import settings
import os

# Step 1: Configure minimal Django settings
settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],  # Directory where HTML templates are stored
}])

# Step 2: Load the HTML file (template)
template_path = os.path.join('templates', 'greeting.html')
with open(template_path, 'r') as file:
    template_content = file.read()

# Step 3: Create Template and Context
template = Template(template_content)
context = Context({'name': 'Alice', 'message': 'Welcome to Django template rendering!'})

# Step 4: Render template
rendered_html = template.render(context)

# Step 5: Output result
print(rendered_html)
