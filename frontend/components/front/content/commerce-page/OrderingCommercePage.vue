<template>
  <Select
    v-model="currentSelect"
    prefix="md-funnel"
    class="cust-select-order-commerce-page"
    @on-change="selectOrder"
  >
    <Option v-for="item in orderList" :key="item.value" :value="item.value">
      {{ item.label }}
    </Option>
  </Select>
</template>

<script>
export default {
  data() {
    return {
      orderList: [
        {
          value: 'default',
          label: 'По умолчанию'
        },
        {
          value: 'priceasc',
          label: 'По цене, сначала дешевые'
        },
        {
          value: 'pricedesc',
          label: 'По цене, сначала дорогие'
        },
        {
          value: 'pricem2asc',
          label: 'По цене за кв.м., сначала дешевые'
        },
        {
          value: 'pricem2desc',
          label: 'По цене за кв.м., сначала дорогие'
        },
        {
          value: 'squareasc',
          label: 'По площади, сначала малые'
        },
        {
          value: 'squaredesc',
          label: 'По площади, сначала большие'
        },
        {
          value: 'datecreateasc',
          label: 'По дате добавления, сначала старые'
        },
        {
          value: 'datecreatedesc',
          label: 'По дате добавления, сначала новые'
        }
      ],
      // modelSelect: 'default',
      newParamsForm: {}
    }
  },
  computed: {
    paramsFilter() {
      return this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS']
    },
    currentSelect: {
      get() {
        if (
          typeof this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS']
            .orderId !== 'undefined'
        ) {
          return this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'].orderId
        } else {
          return 'default'
        }
      },
      set(newName) {
        return newName
      }
    }
  },
  mounted() {
    // eslint-disable-next-line no-console
    console.log(this.newParamsForm)
  },
  methods: {
    selectOrder(e) {
      if (this.$route.path === '/commerce') {
        this.newParamsForm = { ...this.paramsFilter }
        this.newParamsForm.orderId = e
        // eslint-disable-next-line no-console
        // console.log(this.newParamsForm)
        this.$store.dispatch(
          'commerce/FETCH_PARAMS_FOR_FILTERS',
          this.newParamsForm
        )
        this.$router.push({ query: this.newParamsForm })
        this.fetchCommerceObj(this.newParamsForm)
      }
    },
    async fetchCommerceObj(params) {
      const searchParams = new URLSearchParams()
      for (const item in params) {
        if (params[item] !== '' && params[item] !== null) {
          searchParams.append(item, params[item])
        }
        // eslint-disable-next-line no-console
        // console.log(this.form[item])
      }
      await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', searchParams)
    }
  }
}
</script>

<style scoped></style>
