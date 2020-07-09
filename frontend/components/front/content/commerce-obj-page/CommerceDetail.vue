<template>
  <div>
    <Row class="mt-3">
      <i-col :xs="24" :sm="8" :md="6" :lg="16">
        <client-only>
          <!--        <app-gallery :images-obj="imagesObj" />-->
          <app-fotorama :images-obj="imagesObj" />
        </client-only>
      </i-col>
    </Row>

    <Row class="mt-3">
      <i-col :xs="24" :sm="8" :md="6" :lg="16">
        <app-description :description-obj="descriptionObj" />
      </i-col>
    </Row>
  </div>
</template>

<script>
// import AppGallery from './Gallery'
import AppFotorama from './Fotorama'
import AppDescription from './Description'
export default {
  components: {
    // AppGallery,
    AppFotorama,
    AppDescription
  },
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  computed: {
    imagesObj() {
      // return {
      //   main_image: this.data.main_image,
      //   main_image_thumb: this.data.main_image_thumb,
      //   images_commercial_estate: this.data.images_commercial_estate
      // }
      return [
        {
          image: this.data.main_image,
          image_thumb: this.data.main_image_thumb
        },
        ...this.data.images_commercial_estate
      ]
    },
    descriptionObj() {
      return {
        is_group_multiple_objs: this.data.is_group_multiple_objs,
        is_sale: this.data.is_sale,
        is_rent: this.data.is_rent,
        cost_of_sale: this.data.cost_of_sale,
        min_cost_of_sale: this.data.min_cost_of_sale,
        max_cost_of_sale: this.data.max_cost_of_sale,
        area: this.data.area,
        min_area: this.data.min_area,
        max_area: this.data.max_area,
        type_commercial_estate: this.data.type_commercial_estate
      }
    }
  },
  mounted() {
    // eslint-disable-next-line no-console
    // console.log(this.data)
  }
}
</script>
