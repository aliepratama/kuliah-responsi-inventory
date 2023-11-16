<script>
import NavBar from './components/NavBar.vue';
export default {
  components: {
    'nav-bar': NavBar,
  },
}
</script>

<template>
  <div>
    <nav-bar/>
    <router-view v-slot="{ Component }">
      <transition name="fade">
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-active{
  transition-delay: 0.3s;
}
</style>
