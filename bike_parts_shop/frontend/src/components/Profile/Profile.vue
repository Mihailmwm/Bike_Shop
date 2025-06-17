<template>
  <div class="profile-container">
    <!-- Профиль и выход -->
    <div class="section" style="border-top:2px solid white;border-right:2px solid white;border-bottom:2px solid white;">
      <h2 class="section-title">Профиль</h2>
      <div>
        <p><strong>Имя пользователя:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
      </div>
      <button @click="logout" class="logout-button">Выйти</button>
    </div>
    <div class="section" style="border-left:2px solid white;"></div>

    <!-- Заказы -->
    <div class="section" style="border-top:2px solid white;border-right:2px solid white;border-bottom:2px solid white;">
      <h3 class="section-title">Ваши заказы</h3>
      <div v-if="orders.length === 0" class="empty-text">У вас ещё нет заказов.</div>
      <div v-else class="orders">
        <div v-for="order in orders" :key="order.id" class="order-card">
          <p class="order-title">Заказ #{{ order.id }} — {{ formatDate(order.created_at) }}</p>
          <p>Статус: {{ order.status.name }}</p>
          <ul class="order-items">
            <li v-for="item in order.items" :key="item.product.id" class="order-item">
              <img :src="getImageUrl(item.product.image)" alt="Product image" class="item-image" />
              <span>{{ item.product.name }} × {{ item.quantity }} = {{ item.quantity * item.price }} руб.</span>
            </li>
          </ul>
          <p class="order-total">Итого: {{ order.total_price }} руб.</p>
        </div>
      </div>
    </div>
    <div class="section" style="border-left:2px solid white;"></div>

    <!-- Отзывы -->
    <div class="section" style="border-top:2px solid white;border-right:2px solid white;border-bottom:2px solid white;">
      <h3 class="section-title">Ваши отзывы</h3>
      <div v-if="reviews.length === 0" class="empty-text">Вы ещё не оставили отзывов.</div>
      <div v-else class="reviews">
        <div v-for="review in reviews" :key="review.id" class="review-card">
          <div class="review-product-info">
            <img
              v-if="review.product_image"
              :src="getImageUrl(review.product_image)"
              alt="Product Image"
              class="review-product-image"
            />
            <strong>{{ review.product_name }}</strong>
          </div>
          <p class="review-text">“{{ review.comment }}”</p>
          <p class="review-rating">Оценка: {{ review.rating }} / 5</p>
          <p class="review-date">{{ formatDate(review.created_at) }}</p>
        </div>
      </div>
    </div>
    <div class="section" style="border-left:2px solid white;"></div>

    <!-- Корзина -->
    <div class="section" style="border-top:2px solid white;border-right:2px solid white;border-bottom:2px solid white;">
      <h3 class="section-title">Корзина</h3>
      <div v-if="cart.length === 0" class="empty-text">Ваша корзина пуста.</div>
      <div v-else class="item-grid">
        <div v-for="item in cart" :key="item.product.id" class="cart-item">
          <ItemCard :product="item.product" />
          <button @click="removeCartItem(item.product.id)" class="remove-btn">Удалить</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import api from '@/axios'
import ItemCard from '@/components/ShopPage/ItemCard.vue'


export default {
  name: 'UserProfile',
  components: { ItemCard },
  data() {
    return {
      user: { username: '', email: '' },
      orders: [],
      cart: [],
      reviews: [],
    }
  },
  methods: {

    async removeCartItem(productId) {
    try {
      await api.delete(`/api/cart/${productId}/`, this.authHeader())
      this.cart = this.cart.filter(i => i.product.id !== productId);
    } catch {
      alert('Не удалось удалить из корзины.');
    }
  },

    getImageUrl(path) {
    if (!path) return ''
    // Пример: если backend работает на порту 8000
    return path.startsWith('http') ? path : `http://localhost:8000${path}`
  },
    authHeader() {
      const token = localStorage.getItem('access_token')
      return { headers: { Authorization: `Bearer ${token}` } }
    },
    async fetchUser() {
      try {
        const res = await api.get('/api/user/', this.authHeader())
        this.user = res.data
      } catch {
        this.$router.push('/login')
      }
    },
    async fetchOrders() {
      try {
        const res = await api.get('/api/orders/', this.authHeader())
        this.orders = res.data
      } catch {
        this.orders = []
      }
    },
    async fetchCart() {
      try {
        const res = await api.get('/api/cart/', this.authHeader())
        this.cart = res.data.items
      } catch {
        this.cart = []
      }
    },
    async fetchReviews() {
      try {
        const res = await api.get('/api/reviews/user/', this.authHeader())
        this.reviews = res.data
      } catch {
        this.reviews = []
      }
    },
    formatDate(datetime) {
      return new Date(datetime).toLocaleString('ru-RU', {
        day: '2-digit', month: '2-digit', year: 'numeric',
        hour: '2-digit', minute: '2-digit'
      })
    },
    async logout() {
      const refresh = localStorage.getItem('refresh_token')
      try {
        await api.post('/api/logout/', { refresh })
      } catch (e) {
        console.error(e)
      }
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      this.$router.push('/login')
    }
  },
  async mounted() {
    await this.fetchUser()
    this.fetchOrders()
    this.fetchCart()
    this.fetchReviews()
  },
}
</script>


<style scoped>

.fav-item {
  position: relative;
}
.remove-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: red;
  color: white;
  border: none;
  padding: 4px 8px;
  cursor: pointer;
}


.review-product-info {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 6px;
}

.review-product-image {
  width: 50px;
  height: 50px;
  object-fit: cover;
  /* border-radius: 4px;
  border: 1px solid #ddd; */
}


.profile-container {
  padding-top: 5em;
  max-width: 800px;
  margin: 40px auto;
  display: flex;
  flex-direction: column;
  /* gap: 2rem; */
}

.section {
  /* background-color: white; */
  /* border-radius: 8px; */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 24px;
}
.section p {
  color: white;
}
.section-title {
  /* font-size: 24px; */
  margin-bottom: 16px;
}

.section-subtitle {
  font-size: 20px;
  margin-bottom: 16px;
}

.logout-button {
  /* margin-top: 16px;
  padding: 10px 16px;
  background-color: #ef4444;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer; */
          margin-top: 2vw;
    padding: 1em 2em;
    /* font-size: 1em; */
    background: transparent;
    border: 2px solid white;
    color: white;
    cursor: pointer;
    max-width: -moz-fit-content;
    max-width: fit-content;
    min-width: -moz-fit-content;
    min-width: fit-content;
    text-decoration: none;
}

.logout-button:hover {
  background-color: #dc2626;
}


.empty-text {
  color: #4b5563;
}

.orders {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.order-card {
  border: 1px solid #ddd;
  /* border-radius: 6px; */
  padding: 16px;
}

.order-title {
  font-weight: 600;
}

.order-items {
  margin-left: 16px;
  margin-top: 8px;
}

.order-total {
  margin-top: 12px;
  font-weight: 600;
}

.item-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}


.order-item {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.item-image {
  width: 128px;
  height: 128px;
  object-fit: cover;
  /* border-radius: 4px;
  border: 1px solid #ddd; */
}

.reviews {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.review-card {
  border: 1px solid #ffffff;
  /* border-radius: 6px; */
  padding: 12px;
  /* background-color: #f9f9f9; */
}

.review-text {
  font-style: italic;
  margin: 4px 0;
}

.review-rating {
  font-weight: bold;
  color: #2546F3;
}

</style>
