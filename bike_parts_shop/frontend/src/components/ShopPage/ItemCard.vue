<!-- ItemCard.vue -->
<template>
  <div class="card" v-if="product">
    <div class="image-container">
      <img :src="product.image || defaultImage" :alt="product.name">
      <div class="details">
        <button @click="showModal = true">
          <p>Подробнее</p>
        </button>
      </div>
    </div>
    <div class="info">
      <p><b>{{ product.name }}</b></p>
      <p v-if="product.stock > 0">В наличии {{ product.stock }} шт</p>
      <p v-else style="color: red;">Нет в наличии</p>
      <!-- <p>{{ product.description }}</p> -->
      <hr>
      <p class="price">{{ product.price }} руб.</p>
      <div class="actions">
  <button @click="addToCart" class="btn-cart">🛒в корзину</button>
</div>
    </div>
    <div>
    <router-link :to="{ name: 'ProductPage', params: { id: product.id } }">
      Подробнее
    </router-link>
  </div>
    <ProductModal v-if="showModal" :product="product" @close="showModal = false" />
  </div>
</template>

<script>
import ProductModal from "@/components/ShopPage/ProductModal.vue";
import axios from 'axios';


export default {
  props: {
    product: Object, // Получаем объект товара
  },
  components: { ProductModal },
  data() {
    return {
      isFavorite: false,
      showModal: false,
      defaultImage: "https://via.placeholder.com/150",
    };
  },

methods: {
    async addToCart() {
      try {
        const token = localStorage.getItem('access_token');
        console.log(token)
        if (!token) {
          alert('Сначала авторизуйтесь.');
          return;
        }

        await axios.post(
          'http://localhost:8000/api/cart/',
          {
            product_id: this.product.id,
            quantity: 1,
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        alert('Товар добавлен в корзину!');
      } catch (error) {
        console.error(error);
        let message = 'Ошибка при добавлении в корзину.';
        if (error.response?.data?.detail) {
          message += `\n${error.response.data.detail}`;
        }
        alert(message);
      }
    },
  },

};
</script>


  
  <style scoped>
.actions {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.btn-cart,
.btn-fav {
  background: transparent;
  border: none;
  font-size: 22px;
  cursor: pointer;
  color: white;
  transition: transform 0.2s;
}

.btn-fav.active {
  color: red;
}

.btn-cart:hover,
.btn-fav:hover {
  transform: scale(1.1);
}

p {
    font-family: "Montserrat", sans-serif;
    font-weight: 400;
    font-size: 18px;
    color: white;
}
        .card {
            /* background: #222; */
            width: 200px;
            /* padding: 10px; */
            /* text-align: center; */
            position: relative;
            overflow: hidden;
        }

        .image-container {
    position: relative;
    overflow: hidden;
}
        .card img {
            width: 100%;
            height: auto;
            background: lightgray;
        }
        .card .info {
            margin-top: 10px;
        }
        .card .details {
            position: absolute;
            bottom: -80px;
            left: 0;
            width: 100%;
            background: rgba(37, 70, 243, 1);
          
            color: black;
            text-align: center;
            padding: 10px;
            transition: bottom 0.3s ease-in-out;
        }
        .card:hover .details {
            bottom: 0;

        }
        .card .details p{
            color: black;
        }

        .card .details button {
    background: none; /* Убираем фон */
    border: none; /* Убираем границу */
    color: white; /* Делаем текст белым */
    font-size: 16px; /* Устанавливаем размер шрифта */
    cursor: pointer; /* Делаем курсор указателем */
    padding: 5px 10px; /* Немного отступов */
}

.card .details button p {
    color: white; /* Делаем текст белым */
    margin: 0; /* Убираем лишние отступы */
}

.card .details button p:hover {
    /* color: rgb(0, 0, 0);  */
    font-weight: bold;

}

.card .details button:hover {
    /* text-decoration: underline;  */
    
}

  </style>