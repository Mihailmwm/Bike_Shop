<template>
  <div class="gear-selector">
    <h2>6-скоростные КПП</h2>

    <div v-if="error" class="error">
      Ошибка: {{ error }}
    </div>
    <div v-else-if="!products.length" class="empty">
      Товары не найдены.
    </div>

    <div class="scroll-container">
      <div class="gradient left"></div>
      <div class="items" ref="scroller">
        <div
          v-for="product in products"
          :key="product.id"
          class="card"
        >
          <div class="image-wrapper">
            <img
              :src="absoluteUrl(product.image)"
              :alt="product.name"
            />
            <div class="badge" :class="product.available ? 'in-stock' : 'out-of-stock'">
              {{ product.available ? 'В наличии' : 'Нет' }}
            </div>
          </div>
          <div class="content">
            <h3>{{ product.name }}</h3>
            <p class="description">{{ product.description }}</p>
            <div class="footerr">
              <span class="price">{{ formattedPrice(product.price) }} ₽</span>
              <button @click="goToProduct(product.id)">Подробнее</button>
            </div>
          </div>
        </div>
      </div>
      <div class="gradient right"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GearSelector',
  data() {
    return {
      products: [],
      error: null
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/products/?speed_count=6')
      .then(res => {
        this.products = res.data;
      })
      .catch(err => {
        this.error = err.message;
      });
  },
  methods: {
    absoluteUrl(path) {
      if (!path) return '';
      return path.startsWith('http') ? path : `http://localhost:8000${path}`;
    },
    formattedPrice(value) {
      return parseFloat(value).toLocaleString('ru-RU', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      });
    },
    goToProduct(id) {
      this.$router.push({ name: 'ProductPage', params: { id } });
    }
  }
};
</script>

<style scoped>
.gear-selector {
  padding: 20px;
  /* background: #fafafa; */
  border-radius: 12px;
}

.gear-selector h2 {
  margin-bottom: 16px;
  font-size: 1.6em;
  color: #ffffff;
}

.error {
  color: #c00;
  margin-bottom: 12px;
}

.empty {
  color: #666;
  margin-bottom: 12px;
}

.scroll-container {
  position: relative;
}

.items {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 24px;
  padding: 8px 0;
}

/* Видимый скроллбар */
.items::-webkit-scrollbar {
  height: 8px;
}
.items::-webkit-scrollbar-track {
  background: #e0e0e0;
  border-radius: 4px;
}
.items::-webkit-scrollbar-thumb {
  background: #b0b0b0;
  border-radius: 4px;
}
.items {
  scrollbar-width: thin;
  scrollbar-color: #000000 #e0e0e000;
}

.card {
  background: #ffffff00;
  /* border-radius: 8px; */
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  flex: 0 0 auto;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
   width: 260px; 
}

.image-wrapper {
  position: relative;
  overflow: hidden;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
.image-wrapper img {
  display: block;
  width: 100%;
  height: auto;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
  padding: 2px 6px;
  font-size: 0.75em;
  color: #fff;
  border-radius: 4px;
}
.badge.in-stock { background: #28a745; }
.badge.out-of-stock { background: #dc3545; }

.content {
  padding: 12px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.content h3 {
  margin: 0 0 8px;
  font-size: 1.1em;
  color: #ffffff;
}

.description {
  flex-grow: 1;
  font-size: 0.9em;
  color: #ebebeb;
  margin-bottom: 12px;
}

.footerr {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: baseline;
}
.price {
  font-weight: bold;
  color: #ffffff;
}

.footerr button {
  /* background: #007bff;
  border: none;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9em; */
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
.footerr button:hover {
  background: #0056b3;
}

/* Градиентные подсказки по бокам */
/* .gradient {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 40px;
  pointer-events: none;
  z-index: 1;
}
.gradient.left {
  left: 0;
  background: linear-gradient(to right, #000000, transparent);
}
.gradient.right {
  right: 0;
  background: linear-gradient(to left, #000000, transparent);
} */
</style>
