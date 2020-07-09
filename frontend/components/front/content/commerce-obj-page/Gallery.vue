<template>
  <div class="thumb-example">
    <!--    <v-gallery-->
    <!--      :images="imageObj"-->
    <!--      :index="index"-->
    <!--      @close="index = null"-->
    <!--    ></v-gallery>-->

    <CoolLightBox
      :items="imageObj"
      :index="index"
      loop="true"
      @close="index = null"
    >
    </CoolLightBox>
    <!-- swiper1 -->
    <swiper
      ref="swiperTop"
      class="swiper gallery-top"
      :options="swiperOptionTop"
    >
      <swiper-slide
        v-for="(image, imageIndex) in thumbImageObj"
        :key="imageIndex"
        class="image"
        @click.native="index = imageIndex"
      >
        <div
          class="image-gallery-blur"
          :style="{
            backgroundImage: `url(${image})`
          }"
        ></div>
        <img :src="image" alt="eqwew" class="image-gallery" />
      </swiper-slide>
      <div
        slot="button-next"
        class="swiper-button-next swiper-button-white"
      ></div>
      <div
        slot="button-prev"
        class="swiper-button-prev swiper-button-white"
      ></div>
    </swiper>
    <!-- swiper2 Thumbs -->
    <swiper
      ref="swiperThumbs"
      class="swiper gallery-thumbs"
      :options="swiperOptionThumbs"
    >
      <swiper-slide
        v-for="(image, imageIndex) in thumbImageObj"
        :key="imageIndex"
        :style="{
          backgroundImage: `url(${image})`
        }"
      >
        <!--        <img :src="image" alt="eqwew" />-->
      </swiper-slide>
      <!--      <swiper-slide class="slide-1"></swiper-slide>-->
      <!--      <swiper-slide class="slide-2"></swiper-slide>-->
      <!--      <swiper-slide class="slide-3"></swiper-slide>-->
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  components: {
    Swiper,
    SwiperSlide
  },
  props: {
    imagesObj: {
      type: Object,
      required: true
    }
  },
  title: 'Thumbs gallery with Two-way control',

  data() {
    return {
      swiperOptionTop: {
        loop: true,
        // loopedSlides: 5, // looped slides should be the same
        spaceBetween: 30,
        slidesPerView: 1,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },
      swiperOptionThumbs: {
        slideToClickedSlide: true,
        // grabCursor: true,
        // loop: true,
        // loopedSlides: 5, // looped slides should be the same
        spaceBetween: 10,
        // centeredSlides: true,
        slidesPerView: 6,
        touchRatio: 0.2
      },

      images: [
        '/media/images/realestate/2020/5/25/85347-724859-kukukuk-chychychy_511x500.jpg',
        'https://static8.depositphotos.com/1145675/836/i/450/depositphotos_8369327-stock-photo-networks-internet-and-here-wireless.jpg',
        'https://klike.net/uploads/posts/2019-03/1551516106_1.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR867rZj08uvTILL_IhBgNiMpug4sLfphXnDVlTgff7QJlIB7LV&usqp=CAU',
        'https://avatars.mds.yandex.net/get-pdb/1649258/d7747967-9aa8-410a-9dbd-8fbbf199e8e5/s600'
      ],
      thumb: [
        '/media/images/realestate/2020/5/25/85347-724859-kukukuk-chychychy_307x300.jpg'
      ],
      index: null
    }
  },
  computed: {
    imageObj() {
      const iimages = []
      iimages.push(this.imagesObj.main_image)
      // eslint-disable-next-line no-console
      // console.log(iimages)
      this.imagesObj.images_commercial_estate.forEach((item) => {
        iimages.push(item.image)
      })
      return iimages
    },
    thumbImageObj() {
      const tthumb = []
      tthumb.push(this.imagesObj.main_image_thumb)
      // eslint-disable-next-line no-console
      // console.log(this.imagesObj.images_commercial_estate)

      this.imagesObj.images_commercial_estate.forEach((item) => {
        tthumb.push(item.image_thumb)
      })
      return tthumb
    }
  },
  mounted() {
    this.$nextTick(() => {
      const swiperTop = this.$refs.swiperTop.$swiper
      const swiperThumbs = this.$refs.swiperThumbs.$swiper
      swiperTop.controller.control = swiperThumbs
      swiperThumbs.controller.control = swiperTop
    })
    // eslint-disable-next-line no-console
    console.log(this.imagesObj)
  }
}
</script>

<style lang="scss" scoped>
.thumb-example {
  height: 380px;
  /*background-color: #000;*/
}
.image-gallery-blur {
  filter: blur(20px);
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
}

.swiper {
  .swiper-slide {
    background-size: cover;
    background-position: center;
    /*filter: blur(20px);*/
    display: flex;
    justify-content: center;
    align-items: center;
  }

  &.gallery-top {
    height: 80%;
    width: 100%;
  }
  &.gallery-thumbs {
    height: 20%;
    box-sizing: border-box;
    padding: 10px 0;
  }
  &.gallery-thumbs .swiper-slide {
    width: 15%;
    /*height: 100%;*/
    height: 76px;
    opacity: 0.4;
  }
  &.gallery-thumbs .swiper-slide-active {
    opacity: 1;
  }
}
</style>
