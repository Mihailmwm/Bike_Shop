<template>
    <div class="product-detail">
      <h1>{{ product.name }}</h1>
  
      <div class="image-slider" v-if="product.images && product.images.length > 0">
        <img :src="product.images[currentImageIndex].image" :alt="product.name" class="product-image" />
        <div class="slider-buttons">
          <button @click="prevImage">←</button>
          <button @click="nextImage">→</button>
        </div>
        
        <p class="description">{{ product.description }}</p>
        <p class="price">{{ product.price }} ₽</p>
      </div>
      <button class="buy-button" @click="addToCart">Купить</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        product: {},
        currentImageIndex: 0,
      };
    },
    async created() {
      const productId = this.$route.params.id;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/products/${productId}/`);
        console.log(response.data);
        this.product = response.data;
      } catch (error) {
        console.error("Ошибка загрузки товара:", error);
      }
    },
    methods: {
      addToCart() {
        console.log(`Товар "${this.product.name}" добавлен в корзину.`);
      },
      nextImage() {
        if (this.currentImageIndex < this.product.images.length - 1) {
          this.currentImageIndex++;
        } else {
          this.currentImageIndex = 0;
        }
      },
      prevImage() {
        if (this.currentImageIndex > 0) {
          this.currentImageIndex--;
        } else {
          this.currentImageIndex = this.product.images.length - 1;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .product-detail {
    background-color: #000;
    color: #fff;
    padding: 2rem;
    max-width: 800px;
    margin: auto;
    border-radius: 20px;
    padding-top: 8em;
  }
  
  .product-detail h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  .product-image {
    /* width: 100%; */
    max-height: 200px;
    min-height: 200px;
    object-fit: cover;
    border-radius: 12px;
    margin-bottom: 1rem;
  }
  
  .description {
    font-size: 1.1rem;
    margin: 1rem 0;
    color: white;
  }
  
  .price {
    font-size: 1.5rem;
    color: #ffffff;
    margin-bottom: 1rem;
  }
  
  .buy-button {
    padding: 0.75rem 2rem;
    background-color: #1f09c200;
    color: #ffffff;
    border: 1px solid white;
    /* border-radius: 10px; */
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
  }
  
  .buy-button:hover {
    background-color: #1e00ff;
  }
  
  .image-slider {
    position: relative;
    text-align: center;
  }
  
  .slider-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 0.5rem;
  }
  
  .slider-buttons button {
    padding: 0.3rem 0.8rem;
    background-color: #222;
    color: #fff;
    border: 1px solid #555;
    border-radius: 6px;
    cursor: pointer;
  }
  
  .slider-buttons button:hover {
    background-color: #444;
  }
  </style>
  