<template>
  <div>
    <AppMain />
  </div>
</template>
<!-- <script>
 export default {
   name: "HomePage", // Было "Home"
 };


 </script> -->

<script lang="js">
import AppMain from "@/components/Main/AppMain.vue";

export default {
  name: "HomePage",
  components: {
    AppMain,
  },
};
</script>
