<template>
    <div class="contact-form">
      <h2>Свяжитесь с нами</h2>
      <form @submit.prevent="submitForm">
        <div class="section">

          <label >Имя:<input type="text" v-model="form.name" required />
          </label>
        </div>

                <div class="sectionL"></div>

        <div class="section">
        <label>
          Email:
          <input type="email" v-model="form.email"  @blur="validateEmail" :class="{ invalid: emailError }" required />
          <span v-if="emailError" class="error">{{ emailError }}</span>
        </label>
        </div>

                <div class="sectionL"></div>
  <div class="section">

    <label>
      Сообщение:
      <textarea v-model="form.message" required></textarea>
    </label>
  </div>
  
        <button class="otpr" type="submit">Отправить</button>
  
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
          const response = await fetch("/api/contact/send/", {
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

/* Для всех input и textarea автозаполненных браузером */
input:-webkit-autofill,
textarea:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #ffffff00 inset !important; /* прозрачный фон */
  -webkit-text-fill-color: rgb(51, 119, 182) !important;         /* ваш цвет текста */
  transition: background-color 9999s ease-out, color 9999s ease-out;
}

/* Если нужно точечно — для textarea */
textarea:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #ffffff00 inset !important;
  -webkit-text-fill-color: rgb(51, 119, 182) !important;
}



input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #ffffff00 inset !important; 
  -webkit-text-fill-color: rgb(51, 119, 182) !important;        
  transition: background-color 9999s ease-out, color 9999s ease-out;
}

textarea {
      /* font-size: 20px; */
    border: 2px solid white;
    background-color: #ffffff00;
    color: rgb(51, 119, 182);
}
input {
    font-size: 20px;
    border: 2px solid white;
    background-color: #ffffff00;
    color: rgb(51, 119, 182);
}
input p {
    color: white;
}


  .otpr{
        margin-top: 2vw;
    padding: 1em 2em;
    font-size: 1em;
    background: transparent;
    border: 2px solid white;
    color: white;
    cursor: pointer;
    max-width: -moz-fit-content;
    max-width: fit-content;
    min-width: -moz-fit-content;
    min-width: fit-content;
  }
  .contact-form {
/*max-width: 600px; */
    /* margin: auto; */

    /* margin-top: 5em;
    display: flex
;
    padding: 2rem;
    flex-direction: column;
    align-items: center;
        height: 100vh; */

            max-width: 400px; 
    margin: auto; 
    /* padding: 2rem; */
    padding-top: 10em;
    height: 100vh;
  }

.section {
    border-top: 2px solid white;
    border-right: 2px solid white;
    border-bottom: 2px solid white;
}

.sectionL {
    border-left: 2px solid white;
    padding: 40px 0;
}
.section-title {
    font-weight: bold;
    font-size: 18px;
    text-transform: uppercase;
    position: absolute;
    top: -15px;
    left: 20px;
    background: black;
    padding: 5px;
    color: white;
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
    display: flex;
  }

  .invalid {
  border-color: red;
}
  </style>
  