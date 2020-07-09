<template>
  <div class="hero-image">
    <div class="container">
      <div class="title text-center">
        <h1>Вся недвижимость на brokernsk.pro</h1>
      </div>
      <div class="text-center">
        <RadioGroup v-model="selectMode" type="button" class="select-mode">
          <Radio label="Новостройки" class="select-mode-radio"></Radio>
          <Radio label="Коммерческая" class="select-mode-radio"></Radio>
          <Radio label="Загородная" class="select-mode-radio"></Radio>
          <Radio label="Ипотека онлайн" class="select-mode-radio"></Radio>
        </RadioGroup>
      </div>
      <!--      <div v-show="selectMode === 'Коммерческая' ? true : false">-->
      <!--        <div class="search-panel">-->
      <!--          &lt;!&ndash;          <LazyHydrate when-visible>&ndash;&gt;-->
      <!--          <app-main-search-panel-commerce />-->
      <!--          &lt;!&ndash;          </LazyHydrate>&ndash;&gt;-->
      <!--        </div>-->
      <!--      </div>-->
      <!--      <div v-show="selectMode === 'Новостройки' ? true : false">-->
      <!--        <app-search-panel-new-building />-->
      <!--      </div>-->
      <!--      <client-only>-->
      <keep-alive>
        <div v-if="selectMode === 'Новостройки'">
          <app-search-panel-new-building />
        </div>
        <div v-else-if="selectMode === 'Коммерческая'">
          <div class="search-panel">
            <app-main-search-panel-commerce />
          </div>
        </div>
        <!--          <component :is="SearchPanelBuilding"></component>-->
      </keep-alive>
      <!--      </client-only>-->
    </div>
  </div>
</template>

<script>
// import LazyHydrate from 'vue-lazy-hydration'
import AppMainSearchPanelCommerce from '@/components/front/content/search-panels-commerce/MainSearchPanelCommerce'
import AppSearchPanelNewBuilding from '@/components/front/content/search-panels-residential/SearchPanelNewBuilding'
export default {
  name: 'MainView',
  components: {
    // LazyHydrate,
    AppMainSearchPanelCommerce,
    AppSearchPanelNewBuilding
  },
  data() {
    return {
      selectMode: 'Коммерческая'
    }
  }
}
</script>

<style lang="scss" scoped>
.hero-image {
  position: relative;
  /*height: 100vh;*/
  /*min-height: 700px;*/
  height: 600px;
  max-height: 600px;
  background: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.2)),
    url('/media/main_bg.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  color: #fff;
}
.title {
  font-size: 48px;
  line-height: 58px;
  font-weight: 500;
  color: #fff;
  position: relative;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1;
  height: 140px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  text-align: center;
  margin-bottom: 36px;
}
.title h1 {
  font-size: 48px;
  line-height: 47px;
}
.select-mode {
  .select-mode-radio {
    height: 50px !important;
    line-height: 48px;
    padding: 0 35px;
    margin: 0 3px;
    font-size: 16px;
    font-weight: 400;
    background: rgba(0, 0, 0, 0.35);
    color: #fff;
    /*border-color: rgba(0, 0, 0, 0.25);*/
    border: none;
    /*background: none;*/
  }
  .ivu-radio-wrapper-checked {
    border-color: rgba(0, 0, 0, 0.85);
    background: rgba(0, 0, 0, 0.65);
    box-shadow: none;
    &:before {
      background: rgba(0, 0, 0, 0.65);
      /*opacity: 0.1;*/
    }
  }

  .ivu-radio-wrapper:before {
    content: none;
  }
}
.search-panel {
  /*height: 254px;*/
  /*max-height: 254px;*/
  background: #fff;
  padding: 15px;
  margin: 20px auto 0;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.07);
  color: #515a6e;
}
</style>
