<template>
  <div>
    <div>
      <template v-if="descriptionObj.is_sale">
        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <Tag type="border" size="large" color="primary">Продажа</Tag>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div>
              <template v-if="!descriptionObj.is_group_multiple_objs">
                {{ descriptionObj.cost_of_sale | numCredit }} руб.
              </template>
              <template v-else>
                {{ descriptionObj.min_cost_of_sale | numCredit }} -
                {{ descriptionObj.max_cost_of_sale | numCredit }} руб.
              </template>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div>
              <template v-if="!descriptionObj.is_group_multiple_objs">
                {{ descriptionObj.area | numCredit }} м²
              </template>
              <template v-else>
                {{ descriptionObj.min_area | numCredit }} -
                {{ descriptionObj.max_area | numCredit }} м²
              </template>
            </div>
          </i-col>
        </Row>
      </template>

      <template v-if="descriptionObj.is_rent">
        <Tag type="border" size="large" color="primary">Аренда</Tag>
      </template>
    </div>

    Тип недвижимости:
    <span
      v-for="(item, index) in descriptionObj.type_commercial_estate"
      :key="index"
    >
      {{ item
      }}{{
        descriptionObj.type_commercial_estate.length !== index + 1 ? ',' : ''
      }}
    </span>
  </div>
</template>

<script>
export default {
  filters: {
    numCredit(value) {
      return new Intl.NumberFormat().format(value)
    }
  },
  props: {
    descriptionObj: {
      type: Object,
      required: true
    }
  },

  mounted() {
    // eslint-disable-next-line no-console
    console.log(this.descriptionObj)
  }
}
</script>

<style scoped></style>
