<template>
  <div v-if="isVisiblePage" class="text-center">
    <Page
      :total="lenPag"
      :current="currentPage"
      :page-size="8"
      @on-change="changePage"
    />
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  data() {
    return {
      isVisiblePage: false,
      newParamsForm: {}
    }
  },
  computed: {
    countObj() {
      return this.$store.getters['commerce/GET_COUNT_OBJ']
    },
    lenPag() {
      return Math.ceil(this.countObj)
    },
    currentPage() {
      if (
        typeof this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'].page !==
        'undefined'
      ) {
        const page = this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'].page
        return Number(page)
      } else {
        return 1
      }
    },

    paramsFilter() {
      return this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS']
    }
  },
  mounted() {
    if (this.currentPage) {
      this.isVisiblePage = true
    } else {
      this.isVisiblePage = false
    }
  },
  methods: {
    changePage(e) {
      // eslint-disable-next-line no-console
      // console.log(e)

      if (this.$route.path === '/commerce') {
        this.newParamsForm = { ...this.paramsFilter }
        this.newParamsForm.page = String(e)
        // eslint-disable-next-line no-console
        // console.log('this.newParamsForm =>', this.newParamsForm)
        this.$store.dispatch(
          'commerce/FETCH_PARAMS_FOR_FILTERS',
          this.newParamsForm
        )
        // eslint-disable-next-line no-console
        // console.log('this.paramsFilter =>', this.paramsFilter)
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
