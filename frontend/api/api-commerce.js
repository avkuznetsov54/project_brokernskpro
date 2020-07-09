export default class ApiCommerce {
  constructor(ctx) {
    // this.$http = ctx.$http
    this.$axios = ctx.$axios
  }

  getResource = async (url) => {
    // const res = await this.$http.get(`${this._apiBase}${url}`)
    const res = await this.$axios.get(`http://localhost:8000/${url}`)

    if (!res.ok) {
      throw new Error(`Could not fetch ${url}` + `, received ${res.status}`)
    }
    // eslint-disable-next-line no-console
    // console.log(res)
    return await res.json()
  }

  getFilters = async () => {
    const res = await this.getResource(`api/v1/filters/`)
    return await res
  }

  getCommerceCount = async () => {
    const res = await this.getResource(`api/v1/count/`)
    return await res
  }

  getAllCommerce = async (params) => {
    const res = await this.getResource(`api/v1/commerce/all/`, params)
    return await res
  }

  getCommerceDetail = async (id) => {
    const res = await this.getResource(`api/v1/commerce/${id}/`)
    return await res
  }
}
