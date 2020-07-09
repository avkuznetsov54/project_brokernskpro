<template>
  <div>
    <Form ref="form" :model="form" class="form-sale">
      <div>
        <Row class="mb-2">
          <FormItem prop="typeDeal">
            <RadioGroup
              v-model="typeDeal"
              type="button"
              class="select-mode"
              @input="switchSaleRent"
            >
              <Radio label="sale" class="select-mode-radio">Продажа</Radio>
              <Radio label="rent" class="select-mode-radio">Аренда</Radio>
            </RadioGroup>
          </FormItem>
        </Row>
        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <div class="desktop-filter-titles">
                <span>Тип недвижимости</span>
              </div>
              <FormItem prop="typeComEstate">
                <Select
                  v-model="formNum.typeComEstate"
                  multiple
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  @on-select="changeSelectField"
                >
                  <Option
                    v-for="item in valueFilters.type_commercial_estate"
                    :key="item.id"
                    :value="item.name"
                    label="typeComEstate"
                    >{{ item.name }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <div class="desktop-filter-titles">
                <span>Способ покупки</span>
              </div>
              <FormItem prop="purchaseMethod">
                <Select
                  v-model="formNum.purchaseMethod"
                  multiple
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  @on-select="changeSelectField"
                >
                  <Option
                    v-for="item in valueFilters.purchase_method"
                    :key="item.id"
                    :value="item.name"
                    label="purchaseMethod"
                    >{{ item.name }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <template v-if="typeDeal === 'sale'">
              <div class="form-input-wrap">
                <div class="desktop-filter-titles">
                  <span>Стоимость, руб.</span>
                </div>
                <FormItem>
                  <div class="form-input-field">
                    <FormItem prop="minCost">
                      <Input
                        v-model="formNum.minCost"
                        placeholder="От"
                        :maxlength="14"
                        element-id="minCost"
                        @on-change="changeInputNumberField"
                        @keypress.native="onlyNumber"
                      />
                    </FormItem>
                    <FormItem prop="maxCost">
                      <Input
                        v-model="formNum.maxCost"
                        placeholder="До"
                        :maxlength="14"
                        element-id="maxCost"
                        @on-change="changeInputNumberField"
                        @keypress.native="onlyNumber"
                      />
                    </FormItem>
                  </div>
                </FormItem>
              </div>
            </template>
            <template v-else>
              <div class="form-input-wrap">
                <div class="desktop-filter-titles">
                  <span>Стоимость аренды, руб/мес.</span>
                </div>
                <FormItem>
                  <div class="form-input-field">
                    <FormItem prop="minRent">
                      <Input
                        v-model="formNum.minRent"
                        placeholder="От"
                        :maxlength="14"
                        element-id="minRent"
                        @on-change="changeInputNumberField"
                        @keypress.native="onlyNumber"
                      />
                    </FormItem>
                    <FormItem prop="maxRent">
                      <Input
                        v-model="formNum.maxRent"
                        placeholder="До"
                        :maxlength="14"
                        element-id="maxRent"
                        @on-change="changeInputNumberField"
                        @keypress.native="onlyNumber"
                      />
                    </FormItem>
                  </div>
                </FormItem>
              </div>
            </template>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="4">
            <div class="form-input-wrap">
              <div class="desktop-filter-titles">
                <span>Площадь, кв.м.</span>
              </div>
              <FormItem>
                <div class="form-input-field">
                  <FormItem prop="minSquare">
                    <Input
                      v-model="formNum.minSquare"
                      placeholder="От"
                      :maxlength="10"
                      element-id="minSquare"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxSquare">
                    <Input
                      v-model="formNum.maxSquare"
                      placeholder="До"
                      :maxlength="10"
                      element-id="maxSquare"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <div class="desktop-filter-titles">
                <span>Категория бизнеса</span>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <FormItem prop="businessCategory">
                <Select
                  v-model="formNum.businessCategory"
                  multiple
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  @on-select="changeSelectField"
                >
                  <Option
                    v-for="item in valueFilters.business_category"
                    :key="item.id"
                    :value="item.name"
                    label="businessCategory"
                    >{{ item.name }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </i-col>
        </Row>
        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <FormItem prop="changeCities">
                <Select
                  v-model="formNum.changeCities"
                  multiple
                  :max-tag-count="maxTagCount"
                  class="min-text"
                  :max-tag-placeholder="more"
                  placeholder="Город"
                  @on-select="changeSelectField"
                >
                  <Option
                    v-for="item in valueFilters.city"
                    :key="item.id"
                    :value="item.name"
                    label="changeCities"
                    >{{ item.name }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <!--              <client-only>-->
              <FormItem prop="changeDistrict">
                <Select
                  v-model="formNum.changeDistrict"
                  multiple
                  filterable
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  placeholder="Район"
                  @on-select="changeSelectField"
                >
                  <OptionGroup
                    v-for="item in valueFilters.city"
                    :key="item.id"
                    :label="item.name"
                  >
                    <Option
                      v-for="itemCh in item.district_city"
                      :key="itemCh.id"
                      :value="itemCh.name"
                      label="changeDistrict"
                      >{{ itemCh.name }}</Option
                    >
                  </OptionGroup>
                </Select>
              </FormItem>

              <!--              <FormItem prop="changeDistrict">-->
              <!--                <Select-->
              <!--                  v-model="form.changeDistrict"-->
              <!--                  multiple-->
              <!--                  filterable-->
              <!--                  size="large"-->
              <!--                  :max-tag-count="maxTagCount"-->
              <!--                  :max-tag-placeholder="more"-->
              <!--                  placeholder="Район"-->
              <!--                  label-in-value-->
              <!--                  @on-change="changeSelect"-->
              <!--                >-->
              <!--                  <OptionGroup-->
              <!--                    v-for="item in valueFilters.city"-->
              <!--                    :key="item.id"-->
              <!--                    :label="item.name"-->
              <!--                  >-->
              <!--                    <Option-->
              <!--                      v-for="itemCh in item.district_city"-->
              <!--                      :key="itemCh.id"-->
              <!--                      :value="itemCh.name"-->
              <!--                      label="district"-->
              <!--                      >{{ itemCh.name }}-->
              <!--                    </Option>-->
              <!--                  </OptionGroup>-->

              <!--                  <OptionGroup label="Города">-->
              <!--                    <Option-->
              <!--                      v-for="itemCh in valueFilters.city"-->
              <!--                      :key="itemCh.id"-->
              <!--                      :value="itemCh.name"-->
              <!--                      label="city"-->
              <!--                      >{{ itemCh.name }}</Option-->
              <!--                    >-->
              <!--                  </OptionGroup>-->
              <!--                </Select>-->
              <!--              </FormItem>-->
              <!--              </client-only>-->
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap">
              <FormItem prop="changeStreet">
                <Select
                  v-model="formNum.changeStreet"
                  multiple
                  filterable
                  :max-tag-count="maxTagCount"
                  :max-tag-placeholder="more"
                  placeholder="Улица"
                  @on-select="changeSelectField"
                >
                  <Option
                    v-for="item in valueFilters.street"
                    :key="item.id"
                    :value="item.name"
                    label="changeStreet"
                    >{{ item.name }}</Option
                  >
                </Select>
              </FormItem>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="4">
            <div class="form-input-wrap">
              <Button long @click="showExtendedFilter">
                Ещё фильтры
                <Icon
                  :type="isExtendedFilter ? 'ios-arrow-down' : 'ios-arrow-up'"
                />
                <!--            <Icon type="ios-arrow-down" />-->
                <!--            <Icon type="ios-arrow-up" />-->
              </Button>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <Button
              long
              :loading="loadingButton"
              type="success"
              @click="handleSubmit('form')"
            >
              <span v-if="!loadingButton">
                <b>Показать {{ countObj }}</b>
              </span>
            </Button>
          </i-col>
        </Row>
        <Row v-if="tagLine.length !== 0">
          <i-col :xs="24" :sm="8" :md="6" :lg="21">
            <div class="filter-tag-line">
              <div v-for="(item, i) in tagLine" :key="item.label + item.value">
                <Tag v-if="i < 6" class="filter-tag">
                  {{ item.value }}
                  <Icon
                    type="ios-close"
                    @click="handleCloseTag(item.label, item.value, item.tag)"
                  />
                </Tag>
                <Tag v-if="i >= 6 && swichTagVisible" class="filter-tag">
                  {{ item.value }}
                  <Icon
                    type="ios-close"
                    @click="handleCloseTag(item.label, item.value, item.tag)"
                  />
                </Tag>
              </div>
              <div>
                <Tag
                  v-if="tagLine.length > 6"
                  color="#838c91"
                  class="close-tag-line"
                  @click.native="changeSwichTagVisible"
                >
                  {{
                    swichTagVisible
                      ? 'Скрыть'
                      : 'Ещё + ' + String(tagLine.length - 6)
                  }}

                  <Icon
                    :type="swichTagVisible ? 'ios-arrow-up' : 'ios-arrow-down'"
                  />
                </Tag>
              </div>
            </div>
          </i-col>
          <!--          <i-col :xs="24" :sm="8" :md="6" :lg="{ span: 3, offset: 21 }">-->
          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <Button
              size="small"
              :style="{ float: 'right' }"
              @click="handleReset('form')"
            >
              <Icon type="md-trash" />
              Очистить всё
            </Button>
          </i-col>
        </Row>
      </div>
      <div
        class="desktop-extended-filter-modal-block"
        :class="{ hidden: isExtendedFilter }"
      >
        <div class="icon-close-extended-filter" @click="showExtendedFilter">
          <Icon type="ios-close" />
        </div>

        <template v-if="typeDeal === 'sale'">
          <Row>
            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Стоимость, руб/кв.м.</span>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minCostSquare">
                    <Input
                      v-model="formNum.minCostSquare"
                      placeholder="От"
                      :maxlength="10"
                      element-id="minCostSquare"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxCostSquare">
                    <Input
                      v-model="formNum.maxCostSquare"
                      placeholder="До"
                      :maxlength="10"
                      element-id="maxCostSquare"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>
            <i-col :xs="24" :sm="8" :md="6" :lg="5">
              <div class="form-input-wrap-extended-filter">
                <FormItem prop="checkRent">
                  <Checkbox
                    id="checkRent"
                    v-model="formNum.checkRent"
                    size="default"
                    @change.native="changeCheckboxField"
                  >
                    Возможность арендовать
                  </Checkbox>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </FormItem>
              </div>
            </i-col>
          </Row>
          <Row class="mb-25">
            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Возможный доход,<br />руб/мес.</span>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minPossibleIncome">
                    <Input
                      v-model="formNum.minPossibleIncome"
                      placeholder="От"
                      :maxlength="10"
                      element-id="minPossibleIncome"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxPossibleIncome">
                    <Input
                      v-model="formNum.maxPossibleIncome"
                      placeholder="До"
                      :maxlength="10"
                      element-id="maxPossibleIncome"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>

            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Окупаемость, лет</span>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minPayback">
                    <Input
                      v-model="formNum.minPayback"
                      placeholder="От"
                      :maxlength="3"
                      element-id="minPayback"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxPayback">
                    <Input
                      v-model="formNum.maxPayback"
                      placeholder="До"
                      :maxlength="3"
                      element-id="maxPayback"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>

            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Средняя арендная<br />ставка, руб/мес.</span>
                  <Tooltip
                    placement="top"
                    content="При сдаче в аренду после покупки."
                  >
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </div>
                <div class="form-input-field">
                  <FormItem prop="minAverageRentalRate">
                    <Input
                      v-model="formNum.minAverageRentalRate"
                      placeholder="От"
                      :maxlength="10"
                      element-id="minAverageRentalRate"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxAverageRentalRate">
                    <Input
                      v-model="formNum.maxAverageRentalRate"
                      placeholder="До"
                      :maxlength="10"
                      element-id="maxAverageRentalRate"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>
          </Row>
        </template>
        <template v-else>
          <Row>
            <i-col :xs="24" :sm="8" :md="6" :lg="8">
              <div class="form-input-wrap-extended-filter">
                <div class="form-input-title">
                  <span>Стоимость аренды,<br />руб/кв.м.</span>
                </div>
                <div class="form-input-field">
                  <FormItem prop="rent_price_sq_m">
                    <Input
                      v-model="formNum.min_rent_price_sq_m"
                      placeholder="От"
                      :maxlength="10"
                      element-id="min_rent_price_sq_m"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                  <FormItem prop="maxCostSquare">
                    <Input
                      v-model="formNum.max_rent_price_sq_m"
                      placeholder="До"
                      :maxlength="10"
                      element-id="max_rent_price_sq_m"
                      @on-change="changeInputNumberField"
                      @keypress.native="onlyNumber"
                    />
                  </FormItem>
                </div>
              </div>
            </i-col>

            <i-col :xs="24" :sm="8" :md="6" :lg="5">
              <div class="form-input-wrap-extended-filter">
                <FormItem prop="checkSale">
                  <Checkbox
                    id="checkSale"
                    v-model="formNum.checkSale"
                    size="default"
                    @change.native="changeCheckboxField"
                    >Возможность продажи
                  </Checkbox>
                  <Tooltip placement="top" content="Описание что это такое.">
                    <Icon
                      type="ios-information-circle-outline"
                      class="icon-class"
                    />
                  </Tooltip>
                </FormItem>
              </div>
            </i-col>
          </Row>
        </template>

        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="severalFloors">
                <Checkbox
                  id="severalFloors"
                  v-model="formNum.severalFloors"
                  size="default"
                  @change.native="changeCheckboxField"
                >
                  <!--                <span>Помещение с несколькими этажами</span>-->
                  <span>Помещение имеет несколько этажей</span>
                  <!--                Несколько этажей-->
                </Checkbox>
              </FormItem>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="groundFloor">
                <Checkbox
                  id="groundFloor"
                  v-model="formNum.groundFloor"
                  size="default"
                  @change.native="changeCheckboxField"
                  >Цоколь</Checkbox
                >
              </FormItem>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="basement">
                <Checkbox
                  id="basement"
                  v-model="formNum.basement"
                  size="default"
                  @change.native="changeCheckboxField"
                  >Подвал</Checkbox
                >
              </FormItem>
            </div>
          </i-col>
        </Row>
        <Row class="mb-25">
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Этаж</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="minFloor">
                  <Input
                    v-model="formNum.minFloor"
                    placeholder="От"
                    :maxlength="3"
                    element-id="minFloor"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumberAndMinus"
                  />
                </FormItem>
                <FormItem prop="maxFloor">
                  <Input
                    v-model="formNum.maxFloor"
                    placeholder="До"
                    :maxlength="3"
                    element-id="maxFloor"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Этажность</span>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <div class="form-input-field">
                <FormItem prop="minNumberStoreys">
                  <Input
                    v-model="formNum.minNumberStoreys"
                    placeholder="От"
                    :maxlength="3"
                    element-id="minNumberStoreys"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxNumberStoreys">
                  <Input
                    v-model="formNum.maxNumberStoreys"
                    placeholder="До"
                    :maxlength="3"
                    element-id="maxNumberStoreys"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>

        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Расположение,<br />линия</span>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <div class="form-input-field">
                <FormItem prop="relativeLocation">
                  <Select
                    v-model="formNum.relativeLocation"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.relative_location"
                      :key="item.id"
                      :value="item.name"
                      label="relativeLocation"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Станция метро</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="metroStations">
                  <Select
                    v-model="formNum.metroStations"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.metro_stations"
                      :key="item.id"
                      :value="item.name"
                      label="metroStations"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Расстояние до<br />метро, м.</span>
                <Tooltip placement="top" content="Текст что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </div>
              <div class="form-input-field">
                <FormItem prop="minDistanceToMetro">
                  <Input
                    v-model="formNum.minDistanceToMetro"
                    placeholder="От"
                    :maxlength="6"
                    element-id="minDistanceToMetro"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxDistanceToMetro">
                  <Input
                    v-model="formNum.maxDistanceToMetro"
                    placeholder="До"
                    :maxlength="6"
                    element-id="maxDistanceToMetro"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>
        <Row class="mb-25">
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Бизнес центр</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="businessCenter">
                  <Select
                    v-model="formNum.businessCenter"
                    multiple
                    filterable
                    :max-tag-count="maxTagCount"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.business_center"
                      :key="item.id"
                      :value="item.name"
                      label="businessCenter"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Жилой комплекс</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="changeResComplex">
                  <Select
                    v-model="formNum.changeResComplex"
                    multiple
                    filterable
                    :max-tag-count="maxTagCount"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.residential_complex"
                      :key="item.id"
                      :value="item.name"
                      label="changeResComplex"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Класс жилого<br />комплекса</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="classOfHousing">
                  <Select
                    v-model="formNum.classOfHousing"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.class_of_housing"
                      :key="item.id"
                      :value="item.name"
                      label="classOfHousing"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>

        <Row class="mb-25">
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="buildingCommercialEstate">
                <Checkbox
                  id="buildingCommercialEstate"
                  v-model="formNum.buildingCommercialEstate"
                  size="default"
                  @change.native="changeCheckboxField"
                  >В процессе строительства
                </Checkbox>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="3">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="finishedCommercialEstate">
                <Checkbox
                  id="finishedCommercialEstate"
                  v-model="formNum.finishedCommercialEstate"
                  size="default"
                  @change.native="changeCheckboxField"
                  >Готовое
                </Checkbox>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </FormItem>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Год постройки</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="minYearConstruction">
                  <Input
                    v-model="formNum.minYearConstruction"
                    placeholder="От"
                    :maxlength="4"
                    element-id="minYearConstruction"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxYearConstruction">
                  <Input
                    v-model="formNum.maxYearConstruction"
                    placeholder="До"
                    :maxlength="4"
                    element-id="maxYearConstruction"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>

        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Отделка</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="finishingProperty">
                  <Select
                    v-model="formNum.finishingProperty"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.finishing_property"
                      :key="item.id"
                      :value="item.name"
                      label="finishingProperty"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Системы коммуникаций</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="communicationSystems">
                  <Select
                    v-model="formNum.communicationSystems"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.communication_systems"
                      :key="item.id"
                      :value="item.name"
                      label="communicationSystems"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Вытяжка</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="cookerHood">
                  <Select
                    v-model="formNum.cookerHood"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.cooker_hood"
                      :key="item.id"
                      :value="item.name"
                      label="cookerHood"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>
        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Мощность, кВт</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="minKw">
                  <Input
                    v-model="formNum.minKw"
                    placeholder="От"
                    :maxlength="5"
                    element-id="minKw"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxKw">
                  <Input
                    v-model="formNum.maxKw"
                    placeholder="До"
                    :maxlength="5"
                    element-id="maxKw"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Высота потолков, м.</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="minCeilingHeight">
                  <Input
                    v-model="formNum.minCeilingHeight"
                    placeholder="От"
                    :maxlength="4"
                    element-id="minCeilingHeight"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumberAndDot"
                  />
                </FormItem>
                <FormItem prop="maxCeilingHeight">
                  <Input
                    v-model="formNum.maxCeilingHeight"
                    placeholder="До"
                    :maxlength="4"
                    element-id="maxCeilingHeight"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumberAndDot"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Вход</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="typeEntrance">
                  <Select
                    v-model="formNum.typeEntrance"
                    multiple
                    :max-tag-count="maxTagCount"
                    class="min-text"
                    :max-tag-placeholder="more"
                    @on-select="changeSelectField"
                  >
                    <Option
                      v-for="item in valueFilters.type_entrance"
                      :key="item.id"
                      :value="item.name"
                      label="typeEntrance"
                      >{{ item.name }}</Option
                    >
                  </Select>
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>
        <Row>
          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <FormItem prop="parking">
                <Checkbox
                  id="parking"
                  v-model="formNum.parking"
                  size="default"
                  @change.native="changeCheckboxField"
                >
                  Наличие парковки
                </Checkbox>
                <Tooltip placement="top" content="Описание что это такое.">
                  <Icon
                    type="ios-information-circle-outline"
                    class="icon-class"
                  />
                </Tooltip>
              </FormItem>
            </div>
          </i-col>

          <i-col :xs="24" :sm="8" :md="6" :lg="8">
            <div class="form-input-wrap-extended-filter">
              <div class="form-input-title">
                <span>Количество парковок</span>
              </div>
              <div class="form-input-field">
                <FormItem prop="minParking">
                  <Input
                    v-model="formNum.minParking"
                    placeholder="От"
                    :maxlength="5"
                    element-id="minParking"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
                <FormItem prop="maxParking">
                  <Input
                    v-model="formNum.maxParking"
                    placeholder="До"
                    :maxlength="5"
                    element-id="maxParking"
                    @on-change="changeInputNumberField"
                    @keypress.native="onlyNumber"
                  />
                </FormItem>
              </div>
            </div>
          </i-col>
        </Row>

        <Row class="mb-25" type="flex" justify="end">
          <i-col :xs="24" :sm="8" :md="6" :lg="4">
            <Button :style="{ float: 'right' }" @click="handleReset('form')">
              <Icon type="md-trash" />
              Очистить всё
            </Button>
          </i-col>
          <i-col :xs="24" :sm="8" :md="6" :lg="5">
            <Button
              long
              :loading="loadingButton"
              type="success"
              @click="handleSubmit('form')"
            >
              <span v-if="!loadingButton">
                <b>Показать {{ countObj }}</b>
              </span>
            </Button>
          </i-col>
        </Row>
      </div>
    </Form>
  </div>
</template>

<script>
// import _ from 'lodash'

export default {
  name: 'MainSearchPanel',
  data() {
    return {
      maxTagCount: 0,
      maxTagCountOne: 1,
      maxTagCountDistrict: 1,

      isExtendedFilter: true,
      anyFilters: 'ios-arrow-down',

      loadingButton: false,

      typeDeal: 'sale',
      formNum: {},
      objForCopy: {},
      form: {
        is_sale: true,
        is_switchForm: 'sale'
      },
      mainFormItemForCheck: [
        { label: 'is_sale', checkType: 'boolean' },
        { label: 'is_rent', checkType: 'boolean' },
        { label: 'is_switchForm', checkType: 'string' },
        { label: 'orderId', checkType: 'string' },
        { label: 'page', checkType: 'number', maybeNegative: false }
      ],
      formItemForCheck: [
        {
          label: 'typeComEstate',
          tag: undefined,
          serv: 'type_commercial_estate',
          checkType: 'object'
        },
        {
          label: 'purchaseMethod',
          tag: undefined,
          serv: 'purchase_method',
          checkType: 'object'
        },
        {
          label: 'minCost',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxCost',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'minRent',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxRent',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'minSquare',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxSquare',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'businessCategory',
          tag: undefined,
          serv: 'business_category',
          checkType: 'object'
        },
        {
          label: 'changeCities',
          tag: undefined,
          serv: 'city',
          checkType: 'object'
        },
        {
          label: 'changeDistrict',
          tag: undefined,
          serv: 'district',
          checkType: 'object'
        },
        {
          label: 'changeStreet',
          tag: undefined,
          serv: 'street',
          checkType: 'object'
        },
        {
          label: 'minCostSquare',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxCostSquare',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        { label: 'checkRent', tag: 'boolean', checkType: 'boolean' },
        {
          label: 'minPossibleIncome',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxPossibleIncome',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'minPayback',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'maxPayback',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'minAverageRentalRate',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxAverageRentalRate',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'min_rent_price_sq_m',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'max_rent_price_sq_m',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        { label: 'checkSale', tag: 'boolean', checkType: 'boolean' },
        { label: 'severalFloors', tag: 'boolean', checkType: 'boolean' },
        { label: 'groundFloor', tag: 'boolean', checkType: 'boolean' },
        { label: 'basement', tag: 'boolean', checkType: 'boolean' },
        {
          label: 'minFloor',
          tag: 'number',
          checkType: 'number',
          maybeNegative: true,
          isSeparator: 'none'
        },
        {
          label: 'maxFloor',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'minNumberStoreys',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'maxNumberStoreys',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'relativeLocation',
          tag: undefined,
          serv: 'relative_location',
          checkType: 'object'
        },
        {
          label: 'metroStations',
          tag: undefined,
          serv: 'metro_stations',
          checkType: 'object'
        },
        {
          label: 'minDistanceToMetro',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxDistanceToMetro',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'businessCenter',
          tag: undefined,
          serv: 'business_center',
          checkType: 'object'
        },
        {
          label: 'changeResComplex',
          tag: undefined,
          serv: 'residential_complex',
          checkType: 'object'
        },
        {
          label: 'classOfHousing',
          tag: undefined,
          serv: 'class_of_housing',
          checkType: 'object'
        },
        {
          label: 'buildingCommercialEstate',
          tag: 'boolean',
          checkType: 'boolean'
        },
        {
          label: 'finishedCommercialEstate',
          tag: 'boolean',
          checkType: 'boolean'
        },
        {
          label: 'minYearConstruction',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'maxYearConstruction',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'finishingProperty',
          tag: undefined,
          serv: 'finishing_property',
          checkType: 'object'
        },
        {
          label: 'communicationSystems',
          tag: undefined,
          serv: 'communication_systems',
          checkType: 'object'
        },
        {
          label: 'cookerHood',
          tag: undefined,
          serv: 'cooker_hood',
          checkType: 'object'
        },
        {
          label: 'minKw',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxKw',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'minCeilingHeight',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'maxCeilingHeight',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'none'
        },
        {
          label: 'typeEntrance',
          tag: undefined,
          serv: 'type_entrance',
          checkType: 'object'
        },
        { label: 'parking', tag: 'boolean', checkType: 'boolean' },
        {
          label: 'minParking',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        },
        {
          label: 'maxParking',
          tag: 'number',
          checkType: 'number',
          maybeNegative: false,
          isSeparator: 'space'
        }
      ],
      tagLine: [],
      swichTagVisible: false,

      typingTimerInputField: {},
      typingTimerCheckBoxField: {}
    }
  },

  computed: {
    allFormItem() {
      return [...this.mainFormItemForCheck, ...this.formItemForCheck]
    },
    valueFilters() {
      return this.$store.getters['commerce/GET_VALUE_FILTERS']
    },
    countObj() {
      return this.$store.getters['commerce/GET_COUNT_OBJ']
    },
    chechNewQuery() {
      return this.$store.getters['commerce/GET_CHECK_NEW_QUERY']
    },
    paramsFilter() {
      return this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS']
    },
    getTagLine() {
      return this.$store.getters['commerce/GET_TAG_LINE']
    }
  },

  watch: {
    chechNewQuery(newValue) {
      this.loadingButton = false
    }
  },

  async mounted() {
    this.typeDeal = this.$store.getters['commerce/GET_SWITCH_SALE_RENT']

    if (
      Object.keys(this.$store.getters['commerce/GET_VALUE_FILTERS']).length ===
      0
    ) {
      await this.$store.dispatch('commerce/FETCH_VALUE_FILTERS')
    }

    if (
      Object.keys(this.$store.getters['commerce/GET_PARAMS_FOR_FILTERS'])
        .length !== 0
    ) {
      this.form = { ...this.paramsFilter }
      // this.formNum = this.paramsFilter
      this.formNum = { ...this.paramsFilter }
    }
    // // eslint-disable-next-line no-console
    // console.log(this.paramsFilter)

    if (this.$store.getters['commerce/GET_TAG_LINE'].length !== 0) {
      this.tagLine = [...this.getTagLine]
    }

    if (this.$route.path !== '/commerce') {
      if (this.$store.getters['commerce/FETCH_COMMERCE_OBJ'] == null) {
        await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', {
          is_sale: true,
          is_switchForm: 'sale'
        })
      }
      this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', {
        is_sale: true,
        is_switchForm: 'sale'
      })
      // this.getConsolLog()
    } else if (this.$route.path === '/commerce') {
      if (Object.keys(this.$route.query).length === 0) {
        // если query-параметры пусты, то получаем из api объекты
        // eslint-disable-next-line no-console
        // console.log('mounted, query.length === 0')
        if (this.$store.getters['commerce/FETCH_COMMERCE_OBJ'] == null) {
          await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', {
            is_sale: true,
            is_switchForm: 'sale'
          })
        }
        this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', {
          is_sale: true,
          is_switchForm: 'sale'
        })
      } else {
        // если query-параметры есть
        // eslint-disable-next-line no-console
        // console.log('mounted, query.length > 0')

        const qp = {}
        const query = this.$route.query

        for (const item in query) {
          if (query[item] === 'true') {
            // преобразуем строку со значением 'true' в Boolean
            query[item] = true
          } else if (query[item] === 'false') {
            // пропускаем такие параметры
            continue
          } else if (query[item] === '') {
            // пропускаем такие параметры
            continue
          }
          qp[item] = query[item]
        }
        if (query.is_rent) {
          this.typeDeal = 'rent'
          qp.is_rent = true
          qp.is_switchForm = 'rent'
          this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', this.typeDeal)
        } else {
          this.typeDeal = 'sale'
          qp.is_sale = true
          qp.is_switchForm = 'sale'
          this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', this.typeDeal)
        }

        // eslint-disable-next-line no-unused-vars
        const clearQP = this.mainHandlerUrlQueryParams(qp)

        this.$router.push({ query: clearQP })

        if (this.$store.getters['commerce/FETCH_COMMERCE_OBJ'] == null) {
          this.fetchCommerceObj(clearQP) // на api запрос

          this.form = { ...clearQP }
          this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)

          this.formNum = this.processingValuesForDisplay(clearQP)

          if (this.$store.getters['commerce/GET_TAG_LINE'].length === 0) {
            this.handlerQueryParamsToTagLine(
              this.processingValuesForDisplay(clearQP)
            )
          }

          // this.getConsolLog()
        }
      }
    }
  },

  methods: {
    changeSwichTagVisible() {
      this.swichTagVisible = !this.swichTagVisible
    },
    thousandSeparator(newValue) {
      if (newValue !== undefined) {
        const value = newValue
          .replace(/\D/g, '')
          .replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
        // console.log("thousandSeparator => " + v);
        return value
      }
      return newValue
    },
    showExtendedFilter() {
      this.isExtendedFilter = !this.isExtendedFilter
    },
    onlyNumber($event) {
      // console.log($event.keyCode); //keyCodes value
      const keyCode = $event.keyCode ? $event.keyCode : $event.which
      if (keyCode < 48 || (keyCode > 57 && keyCode !== 46)) {
        $event.preventDefault()
      }
    },
    onlyNumberAndMinus($event) {
      // eslint-disable-next-line no-console
      // console.log($event.key, $event.keyCode) // keyCodes value
      const keyCode = $event.keyCode ? $event.keyCode : $event.which
      if (
        // keyCode < 48 || (keyCode > 57 && keyCode !== 46)
        keyCode !== 45 &&
        (keyCode < 48 || keyCode > 57)
      ) {
        $event.preventDefault()
      }
    },
    onlyNumberAndDot($event) {
      // console.log($event.keyCode); //keyCodes value
      const keyCode = $event.keyCode ? $event.keyCode : $event.which
      if (
        (keyCode < 48 || keyCode > 57) &&
        keyCode !== 46 &&
        keyCode !== 190 &&
        keyCode !== 55
      ) {
        $event.preventDefault()
      }
    },
    more(num) {
      return 'Выбрано: ' + num
    },

    handleSubmit(name) {
      if (this.$route.path !== '/commerce') {
        this.$store.dispatch('commerce/FETCH_TAG_LINE', this.tagLine)
        this.$router.push({ path: '/commerce', query: this.form })
      }
      this.getConsolLog()
    },
    handleReset(name) {
      // очищаем поля формы кроме если is_sale=true или is_rent=true
      const keys = Object.keys(this.form)
      keys.forEach((key) => {
        if (key === 'is_sale' && this.form.is_sale) {
          this.form = { is_sale: true, is_switchForm: 'sale' }
          // this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
        } else if (key === 'is_rent' && this.form.is_rent) {
          this.form = { is_rent: true, is_switchForm: 'rent' }
          // this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
        }
      })
      this.tagLine = []
      this.formNum = {}
      this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
      this.fetchCommerceObj(this.paramsFilter)

      if (this.$route.path === '/commerce') {
        this.$router.push({ query: this.paramsFilter })
      }
    },

    switchSaleRent(e) {
      // eslint-disable-next-line no-console
      // console.log(e)

      const arrSale = [
        'minCost',
        'maxCost',
        'minCostSquare',
        'maxCostSquare',
        'checkRent',
        'minPossibleIncome',
        'maxPossibleIncome',
        'minPayback',
        'maxPayback',
        'minAverageRentalRate',
        'maxAverageRentalRate'
      ]
      const arrRent = [
        'minRent',
        'maxRent',
        'min_rent_price_sq_m',
        'max_rent_price_sq_m',
        'checkSale'
      ]

      if (e === 'rent') {
        delete this.form.is_sale
        this.form = { ...this.form, is_rent: true, is_switchForm: 'rent' }
        // this.form.is_rent = true
        // this.form.is_switchForm = 'rent'
        this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', e)

        for (const item in arrSale) {
          delete this.form[arrSale[item]]
          delete this.formNum[arrSale[item]]

          for (const i in this.tagLine) {
            if (this.tagLine[i].label === arrSale[item]) {
              this.tagLine.splice(i, 1)
            }
          }
        }
      } else if (e === 'sale') {
        delete this.form.is_rent
        this.form = { ...this.form, is_sale: true, is_switchForm: 'sale' }
        // this.form.is_sale = true
        // this.form.is_switchForm = 'sale'
        this.$store.dispatch('commerce/FETCH_SWITCH_SALE_RENT', e)

        for (const item in arrRent) {
          delete this.form[arrRent[item]]
          delete this.formNum[arrRent[item]]

          for (const i in this.tagLine) {
            if (this.tagLine[i].label === arrRent[item]) {
              this.tagLine.splice(i, 1)
            }
          }
        }
      }
      this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
      this.fetchCommerceObj(this.paramsFilter)

      if (this.$route.path === '/commerce') {
        this.$router.push({ query: this.paramsFilter })
        // eslint-disable-next-line no-console
        // console.log(this.$router)
      }
    },

    async fetchCommerceObj(params) {
      this.loadingButton = true
      const searchParams = new URLSearchParams()
      for (const item in params) {
        if (params[item] !== '' && params[item] !== null) {
          searchParams.append(item, params[item])
        }
      }
      await this.$store.dispatch('commerce/FETCH_COMMERCE_OBJ', searchParams)
    },

    copyObj(mainObj) {
      const objCopy = {} // objCopy будет хранить копию mainObj

      for (const key in mainObj) {
        // eslint-disable-next-line no-console
        // console.log(mainObj[key], typeof mainObj[key])
        objCopy[key] = mainObj[key] // копирует каждое свойство objCopy
      }
      return objCopy
    },

    changeInputNumberField(e) {
      // eslint-disable-next-line no-console
      // console.log(e.target.value)
      this.formatInputNumber()
      this.handlerInputNumberField(e)

      clearTimeout(this.typingTimerInputField[e.target.id])
      if (e.target.value || e.target.value === '') {
        this.typingTimerInputField[e.target.id] = setTimeout(() => {
          // eslint-disable-next-line no-console
          // console.log('gggggggg')

          this.form[e.target.id] = this.formNum[e.target.id].replace(/\s+/g, '')
          this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
          this.fetchCommerceObj(this.paramsFilter)

          if (this.$route.path === '/commerce') {
            this.$router.push({ query: this.paramsFilter })
            // eslint-disable-next-line no-console
            // console.log(this.$router)
          }
        }, 600)
      }

      // eslint-disable-next-line no-console
      // console.log(this.typingTimerInputField)
    },
    handlerInputNumberField(e) {
      // eslint-disable-next-line no-console
      // console.log(e)
      // console.log(e.target.id, e.target.value)

      const query = { label: e.target.id }
      let targetValue
      if (
        e.target.id !== 'minPayback' &&
        e.target.id !== 'maxPayback' &&
        e.target.id !== 'minFloor' &&
        e.target.id !== 'maxFloor' &&
        e.target.id !== 'minNumberStoreys' &&
        e.target.id !== 'maxNumberStoreys' &&
        e.target.id !== 'minYearConstruction' &&
        e.target.id !== 'maxYearConstruction'
      ) {
        targetValue = new Intl.NumberFormat().format(
          e.target.value.replace(/\s+/g, '')
        )
      } else {
        targetValue = e.target.value
      }

      const item = {
        label: e.target.id,
        value: this.determineLabelForValue(e.target.id, targetValue),
        tag: 'number'
      }
      const n = this.searchObjInArray(this.tagLine, query)
      // eslint-disable-next-line no-console
      // console.log(n.length)

      if (n.length === 0) {
        this.tagLine = [...this.tagLine, item]
      } else if (n.length > 0) {
        this.tagLine.forEach((value, index) => {
          if (value.label === item.label) {
            this.tagLine.splice(index, 1, item)
            // eslint-disable-next-line no-console
            // console.log(value, index)
          }
        })
      }

      if (e.target.value === '') {
        this.tagLine.forEach((value, index) => {
          if (value.label === item.label) {
            this.tagLine.splice(index, 1)
          }
        })
      }
      this.formatInputNumber()
    },

    changeCheckboxField(e) {
      // eslint-disable-next-line no-console
      // console.log(
      //   e.target.labels[0].id,
      //   e.target.checked,
      //   e.target.labels[0].textContent.trim()
      // )

      this.handlerCheckboxField(e)

      clearTimeout(this.typingTimerCheckBoxField[e.target.labels[0].id])
      this.typingTimerCheckBoxField[e.target.labels[0].id] = setTimeout(() => {
        if (e.target.checked) {
          this.form[e.target.labels[0].id] = this.formNum[e.target.labels[0].id]
        } else {
          delete this.form[e.target.labels[0].id]
        }

        this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
        this.fetchCommerceObj(this.paramsFilter)

        if (this.$route.path === '/commerce') {
          this.$router.push({ query: this.paramsFilter })
          // eslint-disable-next-line no-console
          // console.log(this.$router)
        }
      }, 600)
    },
    handlerCheckboxField(e) {
      const query = { label: e.target.labels[0].id }
      const item = {
        label: e.target.labels[0].id,
        // value: e.target.labels[0].textContent.trim(),
        value: this.determineLabelForValue(e.target.labels[0].id, 0),
        tag: 'boolean'
      }
      const n = this.searchObjInArray(this.tagLine, query)
      if (e.target.checked) {
        if (n.length === 0) {
          this.tagLine = [...this.tagLine, item]
        }
      } else {
        this.tagLine.forEach((value, key) => {
          if (value.label === item.label) this.tagLine.splice(key, 1)
        })
      }
    },

    changeSelectField(e) {
      // e = { label: "typeComEstate", tag: undefined, value: "Производство" }
      // eslint-disable-next-line no-console
      // console.log('e =>', e)

      // eslint-disable-next-line no-console
      // console.log(this.tagLine)

      const n = this.searchObjInArray(this.tagLine, e)
      // eslint-disable-next-line no-console
      // console.log(n.length)
      if (n.length === 0) {
        this.tagLine = [...this.tagLine, e]
      } else if (n.length > 0) {
        this.tagLine.forEach((value, key) => {
          if (value.label === e.label && value.value === e.value)
            // delete this.tagLine[key]
            this.tagLine.splice(key, 1)
          // eslint-disable-next-line no-console
          // console.log(value, key)
        })
      }
      // eslint-disable-next-line no-console
      // console.log(this.tagLine)

      // добавляем значения в this.formNum с событии @on-select
      if (typeof this.formNum[e.label] !== 'undefined') {
        // ключ есть
        const index = this.formNum[e.label].indexOf(e.value)
        if (index !== -1) {
          this.formNum[e.label].splice(index, 1)
        } else {
          this.formNum[e.label].push(e.value)
        }
      } else {
        // ключа нет
        this.formNum[e.label] = [e.value]
      }

      this.form[e.label] = this.getArrIdsFromValueFilters(
        e.label,
        this.formNum[e.label]
      )
      this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
      this.fetchCommerceObj(this.paramsFilter)

      if (this.$route.path === '/commerce') {
        this.$router.push({ query: this.paramsFilter })
        // eslint-disable-next-line no-console
        // console.log(this.paramsFilter)
      }
      // this.getConsolLog()
    },

    getArrIdsFromValueFilters(key, arr) {
      // меняем velue на id
      const filterKeys = this.formItemForCheck.filter(
        (item) => item.label === key
      )
      const servKey = filterKeys[0].serv
      const servArr = this.valueFilters[servKey]
      let arrIds
      if (typeof arr === 'object') {
        arrIds = arr.map((item) => {
          for (const idx in servArr) {
            if (servArr[idx].name === item) {
              return servArr[idx].id
            }
          }
        })
      } else if (typeof arr === 'string') {
        for (const idx in servArr) {
          if (servArr[idx].name === arr) {
            return [servArr[idx].id]
          }
        }
      }

      return arrIds
    },
    getArrValuesFromValueFilters(key, arr) {
      // eslint-disable-next-line no-console
      // console.log(key, arr)
      const filterKeys = this.formItemForCheck.filter(
        (item) => item.label === key
      )
      const servKey = filterKeys[0].serv
      const servArr = this.valueFilters[servKey]
      let arrValues
      if (typeof arr === 'object') {
        // оставляем в массиве id которые существуют
        const arrExistIds = arr.filter((item) => {
          for (const idx in servArr) {
            if (servArr[idx].id === Number(item)) return true
          }
        })

        // создаем массив со значениями, которые соответствуют id
        arrValues = arrExistIds.map((item) => {
          for (const idx in servArr) {
            if (servArr[idx].id === Number(item)) {
              return servArr[idx].name
            }
          }
        })

        return arrValues
      } else if (typeof arr === 'string') {
        // eslint-disable-next-line no-console
        // console.log('arr =>', arr)
        for (const idx in servArr) {
          if (servArr[idx].id === Number(arr)) {
            arrValues = [servArr[idx].name]
            return arrValues
          }
        }
      }

      // eslint-disable-next-line no-console
      // console.log('arrValues =>', arrValues)
      // return arrValues
    },
    processingValuesForDisplay(obj) {
      // меняем все id на velue в query params url
      const arrItemWithTagUndefined = this.formItemForCheck.filter(
        (item) => item.tag === undefined
      )
      const arrKeysWithTagUndefined = arrItemWithTagUndefined.map((item) => {
        return item.label
      })

      const arrItemWithTagSpace = this.formItemForCheck.filter(
        (item) => item.isSeparator === 'space'
      )
      const arrKeysWithTagSpace = arrItemWithTagSpace.map((item) => {
        return item.label
      })

      for (const idx in obj) {
        if (arrKeysWithTagUndefined.includes(idx)) {
          const n = this.getArrValuesFromValueFilters(idx, obj[idx])
          if (typeof n !== 'undefined') {
            this.objForCopy[idx] = n
          }
        } else if (arrKeysWithTagSpace.includes(idx)) {
          this.objForCopy[idx] = new Intl.NumberFormat().format(
            obj[idx].replace(/\s+/g, '')
          )
        } else {
          // eslint-disable-next-line no-console
          // console.log('нет')
          this.objForCopy[idx] = obj[idx]
        }
      }

      // eslint-disable-next-line no-console
      // console.log('this.objForCopy =>', this.objForCopy)
      return this.objForCopy
    },
    mainHandlerUrlQueryParams(qp) {
      const clearObj = {}

      for (const keyQP in qp) {
        const isCheck = this.allFormItem.filter((item) => item.label === keyQP) // сравниваем ключи

        if (isCheck.length !== 0) {
          // если key есть в проверочном массиве

          const { checkType, maybeNegative = true } = isCheck[0] // тип по которому сравнивать

          if (checkType === 'object') {
            if (typeof qp[keyQP] === 'object') {
              const arr = []
              for (const idx in qp[keyQP]) {
                if (
                  !isNaN(Number(qp[keyQP][idx])) &&
                  Number(qp[keyQP][idx]) >= 0
                ) {
                  arr.push(Number(qp[keyQP][idx]))
                }
              }
              clearObj[keyQP] = arr
            } else if (typeof qp[keyQP] === 'string') {
              if (!isNaN(Number(qp[keyQP])) && Number(qp[keyQP]) >= 0) {
                clearObj[keyQP] = [Number(qp[keyQP])]
              }
            }
          } else if (checkType === 'number') {
            // eslint-disable-next-line valid-typeof,no-lonely-if
            if (typeof qp[keyQP] === 'string') {
              if (!maybeNegative) {
                if (!isNaN(Number(qp[keyQP])) && Number(qp[keyQP]) >= 0) {
                  clearObj[keyQP] = qp[keyQP]
                }
              } else if (maybeNegative) {
                if (!isNaN(Number(qp[keyQP]))) {
                  clearObj[keyQP] = qp[keyQP]
                }
              }
            }
          } else if (checkType === 'boolean') {
            if (typeof qp[keyQP] === 'boolean') {
              // eslint-disable-next-line no-console
              // console.log('boolean =>', qp[keyQP])
              if (qp[keyQP]) {
                clearObj[keyQP] = qp[keyQP]
              }
            }
          } else if (checkType === 'string') {
            if (typeof qp[keyQP] === 'string') {
              if (qp[keyQP] === qp[keyQP].replace(/[\s\W]+/g, '')) {
                clearObj[keyQP] = qp[keyQP]
              }
            }
          }
        } else {
          clearObj[keyQP] = qp[keyQP]
        }
      }
      return clearObj
    },

    searchObjInArray(list, query) {
      // https://ru.stackoverflow.com/questions/810346/js-%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%B9-%D0%B8-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B4%D0%B2%D1%83%D1%85-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2
      return list.filter((item) =>
        Object.keys(query).every((key) => item[key] === query[key])
      )
    },
    formatInputNumber() {
      // const inputName = [
      //   'minCost',
      //   'maxCost',
      //   'minRent',
      //   'maxRent',
      //   'minSquare',
      //   'maxSquare',
      //   'minCostSquare',
      //   'maxCostSquare',
      //   'min_rent_price_sq_m',
      //   'max_rent_price_sq_m',
      //   'minPossibleIncome',
      //   'maxPossibleIncome',
      //   'minAverageRentalRate',
      //   'maxAverageRentalRate',
      //   'minDistanceToMetro',
      //   'maxDistanceToMetro',
      //   'minKw',
      //   'maxKw',
      //   'minParking',
      //   'maxParking'
      // ]
      // eslint-disable-next-line no-console
      // console.log('formatInputNumber')

      const arrItemWithTagSpace = this.formItemForCheck.filter(
        (item) => item.isSeparator === 'space'
      )
      const arrKeys = arrItemWithTagSpace.map((item) => {
        return item.label
      })

      for (const item in arrKeys) {
        if (this.formNum[arrKeys[item]] && this.formNum[arrKeys[item]] !== '') {
          this.formNum[arrKeys[item]] = new Intl.NumberFormat().format(
            this.formNum[arrKeys[item]].replace(/\s+/g, '')
          )
          // this.formNum[arrKeys[item]] = this.thousandSeparator(
          //   this.formNum[arrKeys[item]].replace(/\s+/g, '')
          // )
        }
        // eslint-disable-next-line no-console
        // console.log(item)
      }
      // for (const item in inputName) {
      //   if (this.form[inputName[item]] && this.form[inputName[item]] !== '') {
      //     this.form[inputName[item]] = new Intl.NumberFormat().format(
      //       this.form[inputName[item]].replace(/\s+/g, '')
      //     )
      //   }
      // }
    },
    determineLabelForValue(label, value) {
      if (label === 'minCost') {
        return 'от ' + value + ' руб.'
      } else if (label === 'maxCost') {
        return 'до ' + value + ' руб.'
      } else if (label === 'minRent') {
        return 'Аренда от ' + value + ' руб/мес.'
      } else if (label === 'maxRent') {
        return 'Аренда до ' + value + ' руб/мес.'
      } else if (label === 'minSquare') {
        return 'от ' + value + ' кв.м.'
      } else if (label === 'maxSquare') {
        return 'до ' + value + ' кв.м.'
      } else if (label === 'minCostSquare') {
        return 'от ' + value + ' руб/кв.м.'
      } else if (label === 'maxCostSquare') {
        return 'до ' + value + ' руб/кв.м.'
      } else if (label === 'min_rent_price_sq_m') {
        return 'Аренда от ' + value + ' руб/кв.м.'
      } else if (label === 'max_rent_price_sq_m') {
        return 'Аренда до ' + value + ' руб/кв.м.'
      } else if (label === 'minPossibleIncome') {
        return 'Доход от ' + value + ' руб/мес.'
      } else if (label === 'maxPossibleIncome') {
        return 'Доход до ' + value + ' руб/мес.'
      } else if (label === 'minPayback') {
        return 'Окупаемость от ' + this.ageToStr(value)
      } else if (label === 'maxPayback') {
        return 'Окупаемость от ' + this.ageToStr(value)
      } else if (label === 'minAverageRentalRate') {
        return 'Средняя арендная ставка от ' + value + ' руб/мес.'
      } else if (label === 'maxAverageRentalRate') {
        return 'Средняя арендная ставка до ' + value + ' руб/мес.'
      } else if (label === 'minFloor') {
        return 'Этаж от ' + value
      } else if (label === 'maxFloor') {
        return 'Этаж до ' + value
      } else if (label === 'minNumberStoreys') {
        return 'Этажность от ' + value
      } else if (label === 'maxNumberStoreys') {
        return 'Этажность до ' + value
      } else if (label === 'minDistanceToMetro') {
        return 'Метро от ' + value + ' м.'
      } else if (label === 'maxDistanceToMetro') {
        return 'Метро до ' + value + ' м.'
      } else if (label === 'minYearConstruction') {
        return 'Год постройки от ' + value
      } else if (label === 'maxYearConstruction') {
        return 'Год постройки до ' + value
      } else if (label === 'minKw') {
        return 'Мощность от ' + value + ' кВт'
      } else if (label === 'maxKw') {
        return 'Мощность до ' + value + ' кВт'
      } else if (label === 'minCeilingHeight') {
        return 'Высота потолков от ' + value + ' м.'
      } else if (label === 'maxCeilingHeight') {
        return 'Высота потолков до ' + value + ' м.'
      } else if (label === 'minParking') {
        return 'Парковок от ' + value
      } else if (label === 'maxParking') {
        return 'Парковок до ' + value
      } else if (label === 'checkSale') {
        return 'Возможность продажи'
      } else if (label === 'checkRent') {
        return 'Возможность аренды'
      } else if (label === 'severalFloors') {
        return 'Помещение имеет несколько этажей'
      } else if (label === 'groundFloor') {
        return 'Цоколь'
      } else if (label === 'basement') {
        return 'Подвал'
      } else if (label === 'buildingCommercialEstate') {
        return 'В процессе строительства'
      } else if (label === 'finishedCommercialEstate') {
        return 'Готовое'
      } else if (label === 'parking') {
        return 'Наличие парковки'
      } else {
        return value
      }
    },
    ageToStr(age) {
      let txt
      if (age % 100 === 1) {
        txt = 'года'
      } else if (age % 10 === 1 && age !== '11') {
        txt = 'года'
      } else {
        txt = 'лет'
      }

      return age + ' ' + txt
    },
    handleCloseTag(key, value, tag) {
      // закрываем tag

      // eslint-disable-next-line no-console
      // console.log(key, value, tag)

      if (tag === 'number' || tag === 'boolean') {
        delete this.form[key]
        delete this.formNum[key]
        this.tagLine.forEach((item, index) => {
          if (item.label === key) {
            this.tagLine.splice(index, 1)
          }
        })
      } else {
        // tag === undefined
        const id = this.getArrIdsFromValueFilters(key, value)
        // eslint-disable-next-line no-console
        // console.log(id)
        if (typeof this.form[key] === 'object') {
          this.form[key] = this.form[key].filter((n) => {
            return n !== Number(id[0])
          })
          this.formNum[key] = this.formNum[key].filter((n) => {
            return n !== value
          })
        } else if (typeof this.form[key] === 'string') {
          // eslint-disable-next-line no-console
          // console.log('string')
          delete this.form[key]
          delete this.formNum[key]
        }

        this.tagLine.forEach((item, index) => {
          if (item.label === key && item.value === value) {
            this.tagLine.splice(index, 1)
          }
        })
      }
      this.$store.dispatch('commerce/FETCH_PARAMS_FOR_FILTERS', this.form)
      this.fetchCommerceObj(this.paramsFilter)

      if (this.$route.path === '/commerce') {
        this.$router.push({ query: this.paramsFilter })
        // eslint-disable-next-line no-console
        // console.log(this.$router)
      }
      // this.getConsolLog()
    },
    handlerQueryParamsToTagLine(arr) {
      for (const indexCheck in this.formItemForCheck) {
        // eslint-disable-next-line no-console
        // console.log(this.formItemForCheck[indexCheck])
        if (
          typeof arr[this.formItemForCheck[indexCheck].label] !== 'undefined'
        ) {
          // ключ есть
          const newLabel = this.formItemForCheck[indexCheck].label
          const newTag = this.formItemForCheck[indexCheck].tag
          const newValue = arr[this.formItemForCheck[indexCheck].label]

          // eslint-disable-next-line no-console
          // console.log('ключ есть', newLabel, newValue, newTag)

          if (newTag === 'number') {
            this.tagLine.push({
              label: newLabel,
              tag: newTag,
              value: this.determineLabelForValue(newLabel, newValue)
            })
          } else if (newTag === 'boolean') {
            this.tagLine.push({
              label: newLabel,
              tag: newTag,
              value: this.determineLabelForValue(newLabel, newValue)
            })
          } else if (newTag === undefined) {
            if (typeof newValue === 'string') {
              this.tagLine.push({
                label: newLabel,
                tag: newTag,
                value: newValue
              })
              // eslint-disable-next-line no-console
              // console.log(this.tagLine)
            } else if (typeof newValue === 'object') {
              // eslint-disable-next-line no-console
              // console.log(typeof newValue)

              for (const item in newValue) {
                // eslint-disable-next-line no-console
                // console.log(newValue[item])
                this.tagLine.push({
                  label: newLabel,
                  tag: newTag,
                  value: newValue[item]
                })
              }
            }
          }
        }
        // else {
        //   // ключа нет
        //   // eslint-disable-next-line no-console
        //   console.log('ключа нет')
        // }
      }
      // this.getConsolLog()
    },

    getConsolLog() {
      // eslint-disable-next-line no-console
      console.log('this.tagLine =>', this.tagLine)
      // eslint-disable-next-line no-console
      console.log('this.formNum =>', this.formNum)
      // eslint-disable-next-line no-console
      console.log('this.form =>', this.form)
      // eslint-disable-next-line no-console
      console.log('this.paramsFilter =>', this.paramsFilter)
    }
    // ////
  }
}
</script>

<style lang="scss" scoped>
.form-sale {
  font-size: 12px;
}
.filter-tag-line {
  /*display: flex;*/
  .filter-tag {
    float: left;
  }
}
.close-tag-line {
  cursor: pointer;
  margin-right: 150px;
}
.form-input-wrap {
  margin-bottom: 24px;
}
.desktop-filter-titles {
  margin-bottom: 10px;
  font-weight: 500;
}
.active-check-button {
  color: #fff;
  background-color: #2d8cf0;
  border-color: #2d8cf0;
  &:hover {
    background-color: #57a3f3;
    border-color: #57a3f3;
  }
}
.ivu-form-item {
  width: 100%;
  margin-bottom: 0 !important;
}
.ivu-checkbox-wrapper {
  font-size: 12px !important;
}
.form-input-field {
  display: flex;
}
.desktop-extended-filter-modal-block {
  position: absolute !important;
  /*max-width: 100%;*/
  width: 1200px;
  /*margin: -5px auto 0px !important;*/
  padding: 30px 20px 0;
  /*border-top: 1px solid #dcdee2;*/
  /*border-radius: 4px;*/
  background-color: #fff;
  box-shadow: 0px 16px 38px rgba(0, 0, 0, 0.12);
  margin-left: -15px;
  z-index: 3;
  margin-top: 16px;

  .form-input-field {
    width: 60%;
  }
}
.icon-close-extended-filter {
  font-size: 56px;
  line-height: 8px;
  position: absolute;
  right: 0;
  top: 18px;
  cursor: pointer;

  .ivu-icon.ivu-icon-ios-close {
    line-height: 0;
  }
}
.icon-class {
  /*border: 1px solid #c5c5c5;*/
  /*border-radius: 10px;*/
  color: #7b7b7b;
  font-size: 15px;
}
.form-input-wrap-extended-filter {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}
</style>
