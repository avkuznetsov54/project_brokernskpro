<template>
  <div class="container my-40">
    <Row>
      <i-col
        v-for="resComplex in resComplexes"
        :key="resComplex.id"
        :xs="24"
        :sm="8"
        :md="6"
        :lg="6"
      >
        <app-residential-complex-card :res-complex="resComplex" />
      </i-col>
    </Row>
  </div>
</template>

<script>
import AppResidentialComplexCard from '@/components/front/content/residential-complex-page/ResidentialComplexCard'
export default {
  name: 'ResidentialComplexListCar2',
  components: {
    AppResidentialComplexCard
  },
  computed: {
    resComplexes() {
      return this.$store.getters['real-estate/GET_RESIDENTIAL_COMPLEXES']
    }
  }
}
</script>

<style scoped></style>
