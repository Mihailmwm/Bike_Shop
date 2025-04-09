<template>
    <div class="contact-form">
      <h2>Свяжитесь с нами</h2>
      <form @submit.prevent="submitForm">
        <label>
          Имя:
          <input type="text" v-model="form.name" required />
        </label>
  
        <label>
          Email:
          <input type="email" v-model="form.email"  @blur="validateEmail" :class="{ invalid: emailError }" required />
          <span v-if="emailError" class="error">{{ emailError }}</span>
        </label>
  
        <label>
          Сообщение:
          <textarea v-model="form.message" required></textarea>
        </label>
  
        <button type="submit">Отправить</button>
  
        <p v-if="successMessage" class="success">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "ContactPage",
    data() {
      return {
        form: {
          name: "",
          email: "",
          message: ""
          
        },
        successMessage: "",
        errorMessage: "",
        emailError: ""
      };
    },
    methods: {
      validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
      if (!emailRegex.test(this.form.email)) {
        this.emailError = "Пожалуйста, введите корректный email.";
      } else {
        this.emailError = "";
      }
    },

      async submitForm() {
        this.validateEmail();
        if (this.emailError) return;

        try {
          console.log("Форма:", this.form);
          const response = await fetch("http://localhost:8000/api/contact/send/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.form)
          });
  
          const data = await response.json();
  
          if (response.ok) {
            this.successMessage = data.message;
            this.errorMessage = "";
            this.form = { name: "", email: "", message: "" };
          } else {
            console.error("Ошибка:", data);  //  Важная строчка для отладки
            this.errorMessage = "Ошибка при отправке формы.";
            this.successMessage = "";
          }
        } catch (err) {
          this.errorMessage = "Сервер недоступен.";
          this.successMessage = "";
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .contact-form {
    max-width: 600px;
    margin: auto;
    padding: 2rem;
  }
  label {
    display: block;
    margin-bottom: 1rem;
  }
  input, textarea {
    width: 100%;
    padding: 0.5rem;
    margin-top: 0.3rem;
  }
  .success {
    color: green;
  }
  .error {
    color: red;
  }

  .invalid {
  border-color: red;
}
  </style>
  