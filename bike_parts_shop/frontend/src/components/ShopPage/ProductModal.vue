<!-- ProductModal.vue -->
<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal">
      <!-- <button class="close-btn" @click="close">&times;</button> -->

      <button class="close-btn" @click="close">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
    <line x1="5" y1="5" x2="19" y2="19"></line>
    <line x1="19" y1="5" x2="5" y2="19"></line>
  </svg>
</button>

      <div class="modal-content">
        <!-- Левая часть - Изображение -->
        <div class="modal-image">
          <button class="nav-btn nav-left" @click="prevImage">&#10094;</button>
          <img :src="currentImage" :alt="product.name">
          <button class="nav-btn nav-right" @click="nextImage">&#10095;</button>


          <!-- Индикаторы (точки) -->
          <div class="dots">
            <span
            v-for="(img, index) in product.images"
            :key="index"
            :class="['dot', { active: index === currentIndex }]"
            @click="setImage(index)"
            ></span>
          </div>

        </div>


        <!-- Правая часть - Информация о товаре -->
        <div class="modal-text">
          <h2>{{ product.name }}</h2>
          <p class="description">{{ product.description }}</p>
          <p class="price">{{ product.price }} ₽</p>
          <button class="buy-button" @click="addToCart">Купить</button>
          <router-link :to="`/product/${product.id}`" class="details-button">Подробнее</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
  },
  data() {
    return {
      currentIndex: 0, // Индекс текущего изображения
      // defaultImage: new URL('@/assets/img/no-image.png', import.meta.url).href,
    };
  },


  computed: {
    currentImage() {
      return this.product?.images?.length
        ? this.product.images[this.currentIndex].image
        : this.defaultImage;
    },
  },

  methods: {

close() {
      this.$emit("close");
    },
    addToCart() {
      console.log(`Товар "${this.product.name}" добавлен в корзину.`);
    },
    nextImage() {
      if (this.product.images.length) {
        this.currentIndex = (this.currentIndex + 1) % this.product.images.length;
      }
    },
    prevImage() {
      if (this.product.images.length) {
        this.currentIndex =
          (this.currentIndex - 1 + this.product.images.length) % this.product.images.length;
      }
    },
    setImage(index) {
      this.currentIndex = index;
    },
  },
};
</script>

<style scoped>
/* Затемненный фон */
.modal-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

/* Основной блок модального окна */
.modal {
  background: white;
  width: 80%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  position: relative;
  /* border-radius: 10px; */
  overflow: hidden;
}

/* Контент модального окна */
.modal-content {
  display: flex;
}

/* Изображение товара */
.modal-image {
  width: 50%;
  background: lightgray;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.modal-image img {
  width: 100%;
  height: auto;
}

/* Текстовая информация */
.modal-text {
  width: 50%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
h2 {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 10px;
}
.description {
  font-size: 16px;
  margin-bottom: 20px;
}
.price {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 20px;
  border-top: 1px solid black;
  padding-top: 10px;
}

/* Кнопка "Купить" */
.buy-button {
  width: 100%;
  padding: 10px;
  background: #2546F3;
  color: white;
  font-weight: bold;
  border: none;
  cursor: pointer;
  /* border-radius: 5px; */
}

/* Кнопка закрытия */
.close-btn {
  position: absolute;
  top: 10px;
  /* right: 10px; */
  left: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

/* Стрелки */
.nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: black;
}

.nav-left {
  left: 10px;
}

.nav-right {
  right: 10px;
}

/* Индикаторы */
.dots {
  text-align: center;
  margin-top: 10px;
}

.dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 0 5px;
  background-color: gray;
  border-radius: 50%;
  cursor: pointer;
  transition: background 0.3s;
}

.dot.active {
  background-color: black;
}

</style>
