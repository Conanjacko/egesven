window.addToCart = function (producto) {
  const carrito = JSON.parse(localStorage.getItem('cart')) || {}
  carrito[producto.nombre] = producto.id
  localStorage.setItem('cart', JSON.stringify(carrito))
  updateCartCount()
}

function updateCartCount() {
  const carrito = JSON.parse(localStorage.getItem('cart')) || {}
  const cartCount = Object.keys(carrito).length
  const cartElement = document.querySelector('.cart')
  if (cartElement) {
    cartElement.setAttribute('data-count', cartCount)
  }
}

document.addEventListener('DOMContentLoaded', function () {
  updateCartCount()
  const cartLink = document.getElementById('cart-link')
  cartLink.addEventListener('click', function (event) {
    updateCartCount()
    event.preventDefault()

    const carrito = JSON.parse(localStorage.getItem('cart')) || {}

    const carritoStr = encodeURIComponent(JSON.stringify(carrito))

    const url = new URL(
      document.getElementById('cart-link').href,
      window.location.origin
    )
    url.searchParams.append('cart', carritoStr)

    window.location.href = url.toString()
  })

  document
    .getElementById('paymentForm')
    .addEventListener('submit', function (e) {
      e.preventDefault()

      const spinner = document.getElementById('spinner')
      const postPurchase = document.getElementById('post-purchase')

      const form = e.target

      spinner.style.display = 'flex'

      setTimeout(() => {
        const url = new URL(window.location.href)
        url.search = ''
        window.history.replaceState(null, '', url.toString())
        spinner.style.display = 'none'
        document.querySelectorAll('.compra').forEach((element) => {
          element.style.display = 'none'
        })

        const carrito = {}
        localStorage.setItem('cart', JSON.stringify(carrito))
        postPurchase.style.display = 'flex'
        postPurchase.innerText = `Compra exitosa # ${crypto.randomUUID()}`
        form.reset()

        alert('Pago procesado con éxito')
      }, 3000)
    })
})
