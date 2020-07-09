<template>
  <div class="container">
    <app-commerce-detail :data="data" />
  </div>
</template>

<script>
import AppCommerceDetail from '@/components/front/content/commerce-obj-page/CommerceDetail'
export default {
  validate({ params }) {
    return Boolean(params.id)
  },

  components: {
    AppCommerceDetail
  },

  async asyncData({ store, params }) {
    const data = await store.dispatch(
      'commerce/FETCH_COMMERCE_DETAIL',
      params.id
    )
    return { data }
  },
  head() {
    return {
      title: '33333' // Other meta information
      // script: [
      //   {
      //     hid: 'jquery',
      //     src: '/js//jquery-1.12.4/jquery.min.js',
      //     defer: true
      //   },
      //   {
      //     hid: 'fotorama',
      //     src: '/js/fotorama-4.6.4/fotorama.js',
      //     defer: true
      //   }
      // ]
    }
  }
}
</script>

<style lang="scss" scoped></style>
