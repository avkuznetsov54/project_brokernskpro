import ApiCommerce from '@/api/api-commerce'

export default (ctx, inject) => {
  const apiCommerce = new ApiCommerce({ $http: ctx.app.$http })
  ctx.$apiCommerce = apiCommerce
  inject('apiCommerce', apiCommerce)
}
