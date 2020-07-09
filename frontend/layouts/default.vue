<template>
  <div>
    <header>
      <app-top-line />
      <app-nav-bar />
    </header>

    <div>
      <nuxt />
    </div>
    <footer>
      <app-footer />
    </footer>
  </div>
</template>

<script>
import AppTopLine from '@/components/front/header/TopLine'
import AppNavBar from '@/components/front/header/NavBar'
import AppFooter from '@/components/front/footer/Footer'
export default {
  components: {
    AppTopLine,
    AppNavBar,
    AppFooter
  }
}
</script>

<style></style>
