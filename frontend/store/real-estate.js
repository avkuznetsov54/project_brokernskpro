export const state = () => ({
  RESIDENTIAL_COMPLEXES: []
})

export const getters = {
  GET_RESIDENTIAL_COMPLEXES: (state) => state.RESIDENTIAL_COMPLEXES
}

export const mutations = {
  // setError(state, error) {
  //   state.error = error
  // },
  // clearError(state) {
  //   state.error = null
  // }
  SET_RESIDENTIAL_COMPLEXES(state, data) {
    state.RESIDENTIAL_COMPLEXES = data
  }
}

export const actions = {
  async FETCH_RESIDENTIAL_COMPLEXES({ commit }) {
    try {
      // const data = await this.$http.$get('api/v1/residential/complex/all/')
      const data = await this.$apiMain.getAllComplex()
      // eslint-disable-next-line no-console
      // console.log(data)
      commit('SET_RESIDENTIAL_COMPLEXES', data)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_RESIDENTIAL_COMPLEXES => ' + e)
    }
  }
}
