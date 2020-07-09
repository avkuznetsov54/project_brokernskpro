<template>
  <div class="container my-20">
    <Row>
      <i-col span="6">
        <Select v-model="model1" prefix="md-funnel" placeholder="Сортировать">
          <Option
            v-for="item in cityList"
            :key="item.value"
            :value="item.value"
            >{{ item.label }}</Option
          >
        </Select>
      </i-col>
      <i-col span="3" offset="15" class="text-right">
        <Icon type="md-list" class="icon-view-obj" />
        <Icon type="ios-apps" class="icon-view-obj" />
      </i-col>
    </Row>

    <Row class="mt-3">
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
  </div>
</template>

<script>
import AppCommerceCard from '@/components/front/content/commerce-page/CommerceCard'
export default {
  name: 'CommerceListCard',
  components: {
    AppCommerceCard
  },
  data() {
    return {
      cityList: [
        {
          value: '1',
          label: 'По умолчанию'
        },
        {
          value: '2',
          label: 'По цене, сначала дешевые'
        },
        {
          value: '3',
          label: 'По цене, сначала дорогие'
        },
        {
          value: '4',
          label: 'По цене за кв.м., сначала дешевые'
        },
        {
          value: '5',
          label: 'По цене за кв.м., сначала дорогие'
        },
        {
          value: '6',
          label: 'По площади, сначала малые'
        },
        {
          value: '7',
          label: 'По площади, сначала большие'
        },
        {
          value: '8',
          label: 'По дате добавления, сначала старые'
        },
        {
          value: '9',
          label: 'По дате добавления, сначала новые'
        }
      ],
      model1: ''
    }
  },
  computed: {
    comObjs() {
      return this.$store.getters['commerce/GET_COMMERCE_OBJ']
    },
    switchSaleRent() {
      return this.$store.getters['commerce/GET_SWITCH_SALE_RENT']
    }
  },
  watch: {
    switchSaleRent(newValue) {
      // eslint-disable-next-line no-console
      // console.log(newValue)
      this.fetchFilterObjs(newValue)
    }
  },
  // async mounted() {
  //   if (this.$store.getters['commerce/GET_COMMERCE_OBJ'].length === 0) {
  //     await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ')
  //   }
  // },
  methods: {
    async fetchFilterObjs(newValue) {
      const params = new URLSearchParams()
      if (newValue === 'Продажа') {
        // const params = { is_sale: true }
        // await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', params)
        params.append('is_sale', true)
      } else if (newValue === 'Аренда') {
        // const params = { is_rent: true }
        // await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', params)
        params.append('is_rent', true)
      }
      await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', params)
    }
  }
}
</script>

<style lang="scss" scoped>
.icon-view-obj {
  font-size: 22px;
}
</style>
