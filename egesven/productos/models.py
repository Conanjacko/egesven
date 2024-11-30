from django.db import models


class Producto(models.Model):
    nombre = models.CharField("Nombre del producto", max_length=100)
    descripcion = models.TextField("Descripción del producto")
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Stock disponible", default=0)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Carrito(models.Model):
    cliente = models.OneToOneField(
        "users.Cliente",
        on_delete=models.CASCADE,
        related_name="carrito",
    )
    productos = models.ManyToManyField(
        "productos.Producto", through="productos.CarritoProducto"
    )

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return f"Carrito de {self.cliente.usuario.username}"


class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField("Cantidad", default=1)

    class Meta:
        verbose_name = "Producto en Carrito"
        verbose_name_plural = "Productos en Carrito"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
