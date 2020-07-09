<template>
  <div
    class="fotorama"
    data-nav="thumbs"
    data-allowfullscreen="true"
    data-loop="true"
    data-width="100%"
    data-height="360"
  >
    <!--    <a-->
    <!--      v-for="(image, imageIndex) in imagesObj"-->
    <!--      :key="imageIndex"-->
    <!--      :href="image.image"-->
    <!--    >-->
    <!--      <div class="1111">-->
    <!--        <img :src="image.image" width="144" height="96" />-->
    <!--      </div>-->
    <!--    </a>-->

    <div
      v-for="(image, imageIndex) in imagesObj"
      :key="imageIndex"
      :data-thumb="image.image_thumb"
      class="panel"
    >
      <div class="image-wrap">
        <div
          class="image-gallery-blur"
          :style="{
            backgroundImage: `url(${image.image_thumb})`
          }"
        ></div>
        <img :src="image.image" class="image" />
      </div>
    </div>

    <!--    <img-->
    <!--      v-for="(image, imageIndex) in imagesLoaded"-->
    <!--      :key="imageIndex"-->
    <!--      :src="image"-->
    <!--    />-->
  </div>
</template>

<script>
export default {
  props: {
    imagesObj: {
      type: Array,
      required: true
    }
  },
  computed: {
    // this property is true when the server sent links to the desired images
    // images are added to the DOM using v-for
    imagesLoaded() {
      // return this.$store.getters.getImagesLoaded
      return [
        '/media/images/realestate/2020/5/25/85347-724859-kukukuk-chychychy_511x500.jpg',
        'https://static8.depositphotos.com/1145675/836/i/450/depositphotos_8369327-stock-photo-networks-internet-and-here-wireless.jpg',
        'https://klike.net/uploads/posts/2019-03/1551516106_1.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR867rZj08uvTILL_IhBgNiMpug4sLfphXnDVlTgff7QJlIB7LV&usqp=CAU',
        'https://avatars.mds.yandex.net/get-pdb/1649258/d7747967-9aa8-410a-9dbd-8fbbf199e8e5/s600'
      ]
    }
    // imageObj() {
    //   const iimages = []
    //   iimages.push(this.imagesObj.main_image)
    //   // eslint-disable-next-line no-console
    //   // console.log(iimages)
    //   this.imagesObj.images_commercial_estate.forEach((item) => {
    //     iimages.push(item.image)
    //   })
    //   return iimages
    // },
    // thumbImageObj() {
    //   const tthumb = []
    //   tthumb.push(this.imagesObj.main_image_thumb)
    //   // eslint-disable-next-line no-console
    //   // console.log(this.imagesObj.images_commercial_estate)
    //
    //   this.imagesObj.images_commercial_estate.forEach((item) => {
    //     tthumb.push(item.image_thumb)
    //   })
    //   return tthumb
    // }
  },
  watch: {
    imagesLoaded(val) {
      if (val) {
        // while fotorama loads from cdn server vue will create img tags using v-for
        this.loadFotorama()
      }
    }
  },
  created() {
    // this.loadJquery()
    // this.loadFotorama()

    this.getFotorama()

    // this.getJquery().then((r) => {
    //   // делаем что-то с содержимым html
    //   return this.getFotorama()
    // })
  },
  mounted() {
    // eslint-disable-next-line no-console
    // console.log(this.imagesObj)
  },
  methods: {
    // // https://fotorama.io/
    // // add script tags to head
    // loadFotorama() {
    //   const script = document.createElement('script')
    //   // script.src =
    //   //   'https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.js'
    //   script.src = '/js/fotorama-4.6.4/fotorama.js'
    //   document.documentElement.firstChild.appendChild(script)
    // },
    // loadJquery() {
    //   const script = document.createElement('script')
    //   // script.src =
    //   //   'https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'
    //   // script.src =
    //   //   'https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'
    //   script.src = '/js//jquery-1.12.4/jquery.min.js'
    //   document.documentElement.firstChild.appendChild(script)
    // }

    getJquery() {
      return new Promise((resolve, reject) => {
        const script = document.createElement('script')
        script.src = '/js//jquery-1.12.4/jquery.min.js'
        document.documentElement.firstChild.appendChild(script)
        resolve(script)
      })
    },

    getFotorama() {
      return new Promise((resolve, reject) => {
        const script = document.createElement('script')
        script.src = '/js/fotorama-4.6.4/fotorama.js'
        document.documentElement.firstChild.appendChild(script)
        resolve(script)
      })
    }
  }
}
</script>

<style scoped>
.image-gallery-blur {
  filter: blur(70px);
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
}

.panel {
  width: 100%;
  height: 100%;
  position: absolute;
}
.image-wrap {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  position: relative;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
}
.image {
  max-width: none;
  max-height: 700px;
  min-width: auto;
  min-height: auto;
  height: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
