<template>
  <div>
    <div class="search-panel-wrap">
      <div class="container">
        <div class="search-panel-page">
          <app-main-search-panel-commerce />
        </div>
      </div>
    </div>
    <div>
      <div class="container">
        <app-commerce-list-card />
      </div>
    </div>
  </div>
</template>

<script>
import AppMainSearchPanelCommerce from '@/components/front/content/search-panels-commerce/MainSearchPanelCommerce'
import AppCommerceListCard from '@/components/front/content/commerce-page/CommerceListCard'

export default {
  components: {
    AppMainSearchPanelCommerce,
    AppCommerceListCard
  }
  // async fetch({ route, store }) {
  //   // eslint-disable-next-line no-console
  //   console.log(route.query)
  //   const params = route.query
  //   const searchParams = new URLSearchParams()
  //   for (const item in params) {
  //     if (params[item] !== '' && params[item] !== null) {
  //       searchParams.append(item, params[item])
  //     }
  //   }
  //   await store.dispatch('commerce/FETCH_COMMERCE_OBJ', searchParams)
  // }
}
</script>

<style lang="scss" scoped>
.search-panel-wrap {
  background: #fff;
  padding: 20px 0;
  /*height: 300px;*/
  border-bottom: 1px solid #d1d5d8;
}
.search-panel-page {
  /*height: 254px;*/
  /*max-height: 254px;*/
  background: #fff;
  padding: 15px;
  /*margin: 20px auto 0;*/
  /*box-shadow: 0 6px 16px rgba(0, 0, 0, 0.07);*/
}
</style>
