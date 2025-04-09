<!--  ContactPage.vue (исправлено) -->

<template>
  <div>
    <!-- Вставь реальный компонент, например ContactForm -->
    <ContactForm />
  </div>
</template>

<script>
import ContactForm from '@/components/ContactForm.vue'; // Импортируешь ДРУГОЙ компонент

export default {
  name: 'ContactPage',
  components: {
    ContactForm
  }
};
</script>
