from django.db import models #Es el scrip donde creamos los modelos es decir, las clases enlazadas a la base de datos

# Create your models here.
#cada vez que se crea un nuevo modelo, se modifica o agrega otro tipo de campo se debe migrar (makemigrateions y luego migrate de la app)

class Project(models.Model):
    title = models.CharField(max_length=180, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción") #campo de texto mas grande
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") #campo de imagen. "upload_to" crea dentro del directorio media una carpeta llamada projects. Se hace esto para que si tenemos otros modelos con el campo image esté mejor organizado y este deparado de otros modelos que pueda existir
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True,) #campo para almacenar enlaces, null y blank true para que pueda esta vacio y no error
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación") #campo de fecha y hora #fecha de creacion. (auto_now_add=true) se añadira la hora automaticamente al crear instancias de proyectos
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modoficación")   #fecha de modificacion o actualizacion. (auto_now=True)se actualizara ela fecha y hora cuando lo modifiquemos
    
    class Meta: #para agregar datos extendidos
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #para ordenar por creacion de mas nuevos a mas antiguos(se agrega "-" para que valla la reverso de la ordenacion, es decir de mas nuevos a mas antiguos)
    
    def __str__(self):
        return self.title