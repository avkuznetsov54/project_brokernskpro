<template>
  <div class="card">
    <div class="card-image">
      <div class="tags-sale-rent">
        <span v-if="comObj.is_sale" class="tag-card">продажа</span>
        <span v-if="comObj.is_rent" class="tag-card">аренда</span>
      </div>

      <div class="card-obj-badge">
        <!--        <Tag class="card-obj-badge-tag" color="primary">{{-->
        <!--          comObj.class_of_housing-->
        <!--        }}</Tag>-->
      </div>

      <div v-if="comObj.images_commercial_estate.length === 0">
        <div class="card-wrap-image" @click="openCard">
          <img
            v-lazy-load
            class="card-image"
            :data-src="comObj.main_image_thumb"
          />
        </div>
      </div>

      <div v-else>
        <!--        <div v-swiper:mySwiper="swiperOption">-->
        <!--          <div class="swiper-wrapper">-->
        <!--            <div class="swiper-slide">-->
        <!--              <div class="card-wrap-image" @click="openCard">-->
        <!--                <img-->
        <!--                  v-lazy-load-->
        <!--                  class="card-image"-->
        <!--                  :data-src="comObj.main_image"-->
        <!--                  :alt="comObj.name"-->
        <!--                />-->
        <!--              </div>-->
        <!--            </div>-->
        <!--            <div-->
        <!--              v-for="img in comObj.images_residential_complex"-->
        <!--              :key="img.id"-->
        <!--              class="swiper-slide"-->
        <!--            >-->
        <!--              <div class="card-wrap-image" @click="openCard">-->
        <!--                <img-->
        <!--                  v-lazy-load-->
        <!--                  class="card-image"-->
        <!--                  :data-src="img.image"-->
        <!--                  :alt="img.alt_attr"-->
        <!--                />-->
        <!--              </div>-->
        <!--            </div>-->
        <!--          </div>-->
        <!--          <div class="swiper-pagination"></div>-->
        <!--          <div class="swiper-button-prev"></div>-->
        <!--          <div class="swiper-button-next"></div>-->
        <!--        </div>-->

        <swiper class="swiper" :options="swiperOption">
          <swiper-slide>
            <div class="card-wrap-image" @click="openCard">
              <img
                v-lazy-load
                class="card-image"
                :data-src="comObj.main_image_thumb"
              />
              <!--              <div class="swiper-lazy-preloader"></div>-->
            </div>
          </swiper-slide>

          <swiper-slide
            v-for="img in comObj.images_commercial_estate"
            :key="img.id"
          >
            <div class="card-wrap-image" @click="openCard">
              <img v-lazy-load class="card-image" :data-src="img.image_thumb" />
              <!--              <div class="swiper-lazy-preloader"></div>-->
            </div>
          </swiper-slide>

          <div slot="pagination" class="swiper-pagination"></div>
          <div slot="button-prev" class="swiper-button-prev"></div>
          <div slot="button-next" class="swiper-button-next"></div>
        </swiper>
      </div>
    </div>
    <div class="card-content" @click="openCard">
      <div class="card-content-title">
        <!--        <p>{{ comObj.cost_of_sale | numCredit }} руб.</p>-->
        <div v-if="switchSaleRent === 'Продажа'">
          <template v-if="!comObj.is_group_multiple_objs">
            <p>{{ comObj.cost_of_sale | numCredit }} руб.</p>
          </template>
          <template v-else>
            <p>
              {{ comObj.min_cost_of_sale | numCredit }} -
              {{ comObj.max_cost_of_sale | numCredit }} руб.
            </p>
          </template>
        </div>
        <div v-else>
          <p>{{ comObj.rent_price_month | numCredit }} руб/мес.</p>
        </div>

        <!--        <span>{{ comObj.area }} м²</span>-->
        <template v-if="!comObj.is_group_multiple_objs">
          <span>{{ comObj.area | numCredit }} м²</span>
        </template>
        <template v-else>
          <span
            >{{ comObj.min_area | numCredit }} -
            {{ comObj.max_area | numCredit }} м²</span
          >
        </template>
      </div>

      <div class="type-obj fz-12 ">
        <template v-if="comObj.type_commercial_estate.length < 3">
          <span
            v-for="(item, index) in comObj.type_commercial_estate"
            :key="index"
          >
            {{ item
            }}{{
              comObj.type_commercial_estate.length !== index + 1 ? ',' : ''
            }}
          </span>
        </template>
        <template v-else>
          <span
            v-for="(item, index) in comObj.type_commercial_estate"
            :key="index"
          >
            <template v-if="index + 1 < 4">
              {{ item }}{{ index + 1 !== 3 ? ',' : ' ...' }}
            </template>
          </span>
        </template>
      </div>

      <div class="fz-12 ">
        Этаж:
        <span v-if="comObj.basement"
          >Подвал{{ comObj.ground_floor ? ', ' : '' }}</span
        >
        <span v-if="comObj.ground_floor"
          >Цоколь{{ comObj.floor.length > 1 ? ', ' : '' }}</span
        >

        <template v-if="comObj.floor.length < 6">
          <span v-for="(item, index) in comObj.floor" :key="index">
            {{ item }}{{ comObj.floor.length !== index + 1 ? ',' : '' }}
          </span>
        </template>
        <template v-else>
          <span v-for="(item, index) in comObj.floor" :key="index">
            <template v-if="index + 1 < 7">
              {{ item }}{{ index + 1 !== 6 ? ',' : ' ...' }}
            </template>
          </span>
        </template>
      </div>

      <div class="card-footer">
        <Divider class="my-1" />
        <div class="card-content-address">
          <span>{{ comObj.city }},</span>
          <span>{{ comObj.district }},</span>
          <div>
            <span>{{ comObj.address }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { directive } from 'vue-awesome-swiper'
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'CommerceCard',
  components: {
    Swiper,
    SwiperSlide
  },
  // directives: {
  //   swiper: directive
  // },
  filters: {
    numCredit(value) {
      return new Intl.NumberFormat().format(value)
    }
  },
  props: {
    comObj: {
      type: Object,
      required: true
    },
    switchSaleRent: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      value1: 0,
      swiperOption: {
        pagination: {
          el: '.swiper-pagination',
          type: 'fraction'
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      }
    }
  },

  mounted() {},

  methods: {
    openCard() {
      // const id = 'test-id'
      this.$router.push(`/commerce/${this.comObj.id}`)
    }
  }
}
</script>

<style lang="scss" scoped>
.card {
  height: 400px;
  margin-bottom: 16px;
  border: 1px solid #eaeaea;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.07);
  transition: box-shadow 0.3s ease-in-out;
  background: #fff;
  &:hover {
    box-shadow: 0 6px 9px rgba(36, 38, 41, 0.16);
  }
  .card-image {
    height: 200px;
    position: relative;
  }
}

.tags-sale-rent {
  position: absolute;
  z-index: 2;
  right: 8px;
  top: 6px;
}
.tag-card {
  color: #ffffff;
  /*font-weight: bold;*/
  font-size: 12px;
  background: rgba(51, 51, 51, 0.75);
  padding: 4px 6px;
  border-radius: 4px;
  cursor: pointer;
}
.card-wrap-image {
  cursor: pointer;
}
.card-obj-badge {
  position: absolute;
  right: 18px;
  top: 5px;
  z-index: 2;
}
.card-obj-badge-tag {
  cursor: default;
}
.swiper-pagination {
  font-size: 14px;
  color: #fff;
}
.swiper-button-prev,
.swiper-button-next {
  background-color: rgba(0, 0, 0, 0.5) !important;
  border-radius: 26px;
  width: 28px;
  height: 28px;
  opacity: 0.2;
  &:hover {
    /*background-color: rgba(0, 0, 0, 0.5) !important;*/
    /*opacity: 0.85;*/
  }
}

/*.swiper-pagination:hover ~ .swiper-button-prev,*/
/*.swiper-pagination:hover ~ .swiper-button-next,*/
/*.swiper-wrapper:hover ~ .swiper-button-prev,*/
/*.swiper-wrapper:hover ~ .swiper-button-next */
.card:hover .swiper-button-prev,
.card:hover .swiper-button-next {
  opacity: 0.95;
}
.swiper-button-disabled {
  display: none;
}
.swiper-button-prev:after,
.swiper-button-next:after {
  font-size: 14px;
  color: #fff;
  font-weight: 900;
}
.swiper-pagination.swiper-pagination-fraction {
  position: absolute;
  background: rgba(51, 51, 51, 0.5);
  border-radius: 4px;
  text-align: center;
  min-width: 40px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 12px;
  left: 15px;
  bottom: 15px;
  z-index: 15;
  width: 15px;
}
.card-wrap-image {
  display: flex;
  justify-content: center; /*центрируем элемент по горизонтали */
  align-items: center; /* и вертикали */
  /*width: auto; !* задали размеры блоку-родителю *!*/
  /*height: 200px;*/
  overflow: hidden; /* если элемент больше блока-родителя – обрезаем лишнее */

  .card-image {
    display: flex;
    flex: 1 1;
    /*padding: 20px;*/
    height: 200px;
    /*border: 1px solid;*/
    align-items: center;

    .card-image img {
      max-width: 100%;
      height: 200px;
      /*overflow: hidden;*/
    }
  }
}
.card-content {
  height: 200px;
  padding: 14px;
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  align-items: flex-start;
  cursor: pointer;
}
.card-content-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}
.type-obj {
  height: 35px;
}
.card-content-address {
  font-size: 14px;
  line-height: 1.4;
  span {
    white-space: nowrap;
  }
}
.card-footer {
  width: 100%;
}
</style>
