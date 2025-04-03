<template>
  <div id="app">
    <header>
      <div class="navbar">
        <div class="header-content">
          <div
            class="wrapper2"
            style="background-color: black;"
          >
            <div class="menu-list2dv">
              <ul class="menu-list2">
                <li>
                  <router-link
                    to="/home"
                    class="menu-item2"
                  >
                    Главная
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/about"
                    class="menu-item2"
                  >
                    О нас
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/process"
                    class="menu-item2"
                  >
                    Процесс
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/shop"
                    class="menu-item2"
                  >
                    Магазин
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/contact"
                    class="menu-item2"
                  >
                    Контакты
                  </router-link>
                </li>
              </ul>
            </div>
          </div>

          <div class="wrapper">
            <div
              class="menu"
              style="z-index: 10;"
            >
              <input
                id="burger-checkbox"
                type="checkbox"
                class="burger-checkbox"
              >
              <label
                for="burger-checkbox"
                class="burger"
                style="color: black;"
              />
              <ul
                class="menu-list"
                style="display: none;"
              > 
                <li>
                  <router-link
                    to="/home"
                    class="menu-item"
                  >
                    Главная
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/about"
                    class="menu-item"
                  >
                    О нас
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/process"
                    class="menu-item"
                  >
                    Процесс
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/shop"
                    class="menu-item"
                  >
                    Магазин
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/contact"
                    class="menu-item"
                  >
                    Контакты
                  </router-link>
                </li>
              </ul>
            </div>
          </div>

          <div class="Logo">
            <img
              src="@/assets/img/Logo.svg"
              alt="Логотип"
            >
          </div>
        </div>
      </div>
    </header>
  </div>
</template>
