import { apiCommerce } from '@/api'

export const state = () => ({
  DATA_VALUE_FILTERS: {},
  DATA_COUNT_OBJ: null,
  DATA_COMMERCE_OBJ: null,
  DATA_SWITCH_SALE_RENT: 'sale',
  DATA_PARAMS_FOR_FILTERS: {},
  DATA_TAG_LINE: []
})

export const getters = {
  GET_VALUE_FILTERS: (state) => state.DATA_VALUE_FILTERS,
  GET_COUNT_OBJ: (state) => state.DATA_COUNT_OBJ,
  GET_COMMERCE_OBJ: (state) => state.DATA_COMMERCE_OBJ,
  GET_CHECK_NEW_QUERY: (state) => state.DATA_COMMERCE_OBJ + Math.random(),
  GET_SWITCH_SALE_RENT: (state) => state.DATA_SWITCH_SALE_RENT,
  GET_PARAMS_FOR_FILTERS: (state) => state.DATA_PARAMS_FOR_FILTERS,
  GET_TAG_LINE: (state) => state.DATA_TAG_LINE
}

export const mutations = {
  SET_VALUE_FILTERS(state, data) {
    state.DATA_VALUE_FILTERS = data
  },
  SET_COUNT_OBJ(state, data) {
    state.DATA_COUNT_OBJ = data
  },
  SET_COMMERCE_OBJ(state, data) {
    state.DATA_COMMERCE_OBJ = data.results
  },
  SET_SWITCH_SALE_RENT(state, data) {
    state.DATA_SWITCH_SALE_RENT = data
  },
  SET_PARAMS_FOR_FILTERS(state, data) {
    state.DATA_PARAMS_FOR_FILTERS = { ...data }
  },
  SET_TAG_LINE(state, data) {
    state.DATA_TAG_LINE = data
  }
}

export const actions = {
  async FETCH_VALUE_FILTERS({ commit }) {
    try {
      // const res = await this.$apiCommerce.getFilters()
      const res = await this.$axios.$get(`${apiCommerce}/api/v1/filters/`)
      commit('SET_VALUE_FILTERS', res)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_VALUE_FILTERS => ' + e)
    }
  },
  // async FETCH_COUNT_OBJ({ commit }, payload) {
  //   try {
  //     const res = await this.$apiCommerce.getCommerceCount()
  //     commit('SET_COUNT_OBJ', res.count)
  //   } catch (e) {
  //     // eslint-disable-next-line no-console
  //     console.log('catch FETCH_COUNT_OBJ => ' + e)
  //   }
  // },
  async FETCH_COMMERCE_OBJ({ commit }, params) {
    try {
      // const data = await this.$http.$get('api/v1/residential/complex/all/')
      // const data = await this.$apiCommerce.getAllCommerce(params)
      const data = await this.$axios.$get(
        `${apiCommerce}/api/v1/commerce/all/`,
        {
          params
        }
      )
      // eslint-disable-next-line no-console
      // console.log('FETCH_COMMERCE_OBJ =>', data)
      commit('SET_COMMERCE_OBJ', data)
      commit('SET_COUNT_OBJ', data.count)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_COMMERCE_OBJ => ' + e)
    }
  },
  async FETCH_COMMERCE_DETAIL({ commit }, id) {
    try {
      // return await this.$apiCommerce.getCommerceDetail(id)
      return await this.$axios.$get(`${apiCommerce}/api/v1/commerce/${id}/`)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_COMMERCE_DETAIL => ' + e)
    }
  },
  FETCH_SWITCH_SALE_RENT({ commit }, payload) {
    try {
      commit('SET_SWITCH_SALE_RENT', payload)
      // eslint-disable-next-line no-console
      // console.log(payload)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_SWITCH_SALE_RENT => ' + e)
    }
  },
  FETCH_PARAMS_FOR_FILTERS({ commit }, payload) {
    try {
      commit('SET_PARAMS_FOR_FILTERS', payload)
      // eslint-disable-next-line no-console
      // console.log(payload)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_PARAMS_FOR_FILTERS => ' + e)
    }
  },
  FETCH_TAG_LINE({ commit }, payload) {
    try {
      commit('SET_TAG_LINE', payload)
      // eslint-disable-next-line no-console
      // console.log(payload)
    } catch (e) {
      // eslint-disable-next-line no-console
      console.log('catch FETCH_TAG_LINE => ' + e)
    }
  }
}
