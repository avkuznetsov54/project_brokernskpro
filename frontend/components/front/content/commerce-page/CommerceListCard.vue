<template>
  <div class="container my-20">
    <Row>
      <i-col span="8">
        <client-only>
          <app-ordering-commerce-page />
        </client-only>
      </i-col>
      <i-col span="3" offset="13" class="text-right">
        <Icon type="md-list" class="icon-view-obj" />
        <Icon type="ios-apps" class="icon-view-obj" />
      </i-col>
    </Row>

    <Row v-if="comObjs" class="mt-3">
      <i-col
        v-for="resObj in comObjs"
        :key="resObj.id"
        :xs="24"
        :sm="8"
        :md="6"
        :lg="6"
      >
        <app-commerce-card
          :com-obj="resObj"
          :switch-sale-rent="switchSaleRent"
        />
      </i-col>
    </Row>

    <Row v-else class="mt-3 spin-loading">
      <Spin size="large"></Spin>
    </Row>

    <Row class="mt-3">
      <i-col span="24">
        <app-pagination />
      </i-col>
    </Row>
  </div>
</template>

<script>
import AppOrderingCommercePage from '@/components/front/content/commerce-page/OrderingCommercePage'
import AppCommerceCard from '@/components/front/content/commerce-page/CommerceCard'
import AppPagination from '@/components/front/content/commerce-page/Pagination'
export default {
  name: 'CommerceListCard',
  components: {
    AppOrderingCommercePage,
    AppCommerceCard,
    AppPagination
  },
  data() {
    return {}
  },
  computed: {
    comObjs() {
      return this.$store.getters['commerce/GET_COMMERCE_OBJ']
    },
    switchSaleRent() {
      return this.$store.getters['commerce/GET_SWITCH_SALE_RENT']
    }
  },

  methods: {}
}
</script>

<style lang="scss" scoped>
.icon-view-obj {
  font-size: 22px;
}
.spin-loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 500px;
}
</style>
