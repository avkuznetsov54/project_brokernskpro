import ApiMain from '@/api/api-main'

export default (ctx, inject) => {
  const apiMain = new ApiMain({ $http: ctx.app.$http })
  ctx.$apiMain = apiMain
  inject('apiMain', apiMain)
}
