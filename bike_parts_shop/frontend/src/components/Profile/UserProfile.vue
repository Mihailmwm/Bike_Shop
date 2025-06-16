<!-- <template>
  <div class="orders-container">
    <h3 class="orders-title">Ваши заказы</h3>
    <div v-if="!orders.length" class="no-orders">У вас ещё нет заказов.</div>
    <div v-for="order in orders" :key="order.id" class="order-card">
      <p><strong>Заказ #{{ order.id }}</strong> — {{ formatDate(order.created_at) }}</p>
      <p>Статус: {{ order.status.name }}</p>
      <ul class="order-items">
        <li v-for="item in order.items" :key="item.product.id">
          {{ item.product.name }} × {{ item.quantity }} = {{ item.price * item.quantity }} руб.
        </li>
      </ul>
      <p class="order-total"><b>Итого:</b> {{ order.total_price }} руб.</p>
    </div>
  </div>
</template>


<script>
import api from '@/axios'

export default {
  data() {
    return { orders: [] }
  },
  async mounted() {
    const { data } = await api.get('/api/orders/', this.authHeader())
    this.orders = data
  },
  methods: {
    authHeader() {
      const token = localStorage.getItem('access_token')
      return { headers: { Authorization: `Bearer ${token}` } }
    },
    formatDate(datetime) {
      return new Date(datetime).toLocaleString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  },
}
</script>

<style scoped>
.orders-container {
  max-width: 800px;
  margin: 40px auto;
  padding: 0 16px;
}

.orders-title {
  font-size: 24px;
  margin-bottom: 16px;
}

.no-orders {
  color: #666;
}

.order-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 24px;
  background-color: #f9f9f9;
}

.order-items {
  margin-left: 16px;
  margin-top: 8px;
  list-style-type: disc;
}

.order-total {
  margin-top: 12px;
  font-weight: bold;
}
</style>
 -->
