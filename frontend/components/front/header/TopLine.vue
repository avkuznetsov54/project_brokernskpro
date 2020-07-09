<template>
  <div class="top-line">
    <div class="container">
      <Row>
        <i-col :xs="24" :sm="16" :md="16" :lg="12">
          <a href="/">
            <div class="main-logo">
              <img src="/media/logo.svg" alt="brokernsk.pro" />
              <!--              <object type="image/svg+xml" data="/media/logo.svg"></object>-->
            </div>
          </a>
        </i-col>
        <i-col :xs="24" :sm="8" :md="8" :lg="{ span: 4, offset: 8 }">
          <Button type="error"><b>ОСТАВИТЬ ЗАЯВКУ</b></Button>
        </i-col>
      </Row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopLine'
}
</script>

<style lang="scss" scoped>
.top-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;
  border-bottom: 1px solid #e6e6e6;
  background: #fff;
}
.main-logo {
  /*display: flex;*/
  img {
    width: 200px;
  }
}
</style>
