// document.querySelector('.burger').addEventListener('click', function () {
//     this.classList.toggle('active');

//     document.querySelector('.menu-list').classList.toggle('open');

// })


// ------------------------------------------
// import { onMounted } from "vue";

// export default {
//   setup() {
//     onMounted(() => {
//       const burger = document.querySelector('.burger');
//       const menuList = document.querySelector('.menu-list');

//       if (burger && menuList) {
//         burger.addEventListener('click', function () {
//           this.classList.toggle('active');
//           menuList.classList.toggle('open');
//         });
//       } else {
//         console.error("Элемент .burger или .menu-list не найден!");
//       }
//     });
//   },
// };
// ////////////////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", function () {
    const burger = document.querySelector('.burger');
    const menuList = document.querySelector('.menu-list');

    if (burger && menuList) {
        burger.addEventListener('click', function () {
            this.classList.toggle('active');
            menuList.classList.toggle('open');
        });
    } else {
        console.error("Элемент .burger или .menu-list не найден!");
    }
});


