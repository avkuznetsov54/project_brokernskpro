export default class ApiMain {
  constructor(ctx) {
    this.$http = ctx.$http
  }

  getResource = async (url) => {
    // const res = await this.$http.get(`${this._apiBase}${url}`)
    const res = await this.$http.get(`http://localhost:8000/${url}`)

    if (!res.ok) {
      throw new Error(`Could not fetch ${url}` + `, received ${res.status}`)
    }
    // eslint-disable-next-line no-console
    // console.log(res)
    return await res.json()
  }

  getAllComplex = async () => {
    const res = await this.getResource(`api/v1/residential/complex/all/`)
    return await res
  }
}
