from django.db.models import Q

from .custom_checks import is_list_int, is_int


def hanler_query_params(queryset, qp):
    print('eee')

    select = {}
    order_by = []
    params = []
    mm_d = {}
    for k, v in qp:
        # if k == "cursor":
        #     continue

        # если 'v' равно пустой строке то прекращаем итерацию
        # чтоб не занести её в queryset, а то 500 error
        if v == '':
            continue

        if k == 'is_sale':
            if v == 'true':
                params.append(Q(is_sale=True))

        if k == 'is_rent':
            if v == 'true':
                params.append(Q(is_rent=True))

        if k == 'checkSale':
            if v == 'true':
                params.append(Q(is_sale=True))

        if k == 'checkRent':
            if v == 'true':
                params.append(Q(is_rent=True))

        if k == 'typeComEstate':
            v = v.split(',')
            n = is_list_int(v)
            if len(n) != 0:
                params.append(Q(type_commercial_estate__in=n))

        if k == 'purchaseMethod':
            v = v.split(',')
            n = is_list_int(v)
            if len(n) != 0:
                params.append(Q(purchase_method__in=v))

        if k == 'minCost':
            v = is_int(v)
            if v:
                # params.append(Q(cost_of_sale__gte=v))
                mm_d.update({'min_cost': v})

        if k == 'maxCost':
            v = is_int(v)
            if v:
                # params.append(Q(cost_of_sale__lte=v))
                mm_d.update({'max_cost': v})

        if k == 'minRent':
            v = is_int(v)
            if v:
                params.append(Q(rent_price_month__gte=v))
        if k == 'maxRent':
            v = is_int(v)
            if v:
                params.append(Q(rent_price_month__lte=v))

        if k == 'businessCategory':
            v = v.split(',')
            n = is_list_int(v)
            if len(n) != 0:
                params.append(Q(business_category__in=v))

        if k == 'orderId':
            if v == 'priceasc':
                select = {'sort_order': 'COALESCE(cost_of_sale,min_cost_of_sale)'}
                order_by = ['sort_order']
            if v == 'pricedesc':
                select = {'sort_order': 'COALESCE(cost_of_sale,max_cost_of_sale)'}
                order_by = ['-sort_order']

    if 'min_cost' in mm_d and 'max_cost' in mm_d:
        params.append(
            ((Q(min_cost_of_sale__gte=mm_d['min_cost']) & Q(min_cost_of_sale__lte=mm_d['max_cost'])) |
             (Q(max_cost_of_sale__gte=mm_d['min_cost']) & Q(max_cost_of_sale__lte=mm_d['max_cost'])) |
             (Q(min_cost_of_sale__gte=mm_d['min_cost']) & Q(max_cost_of_sale__lte=mm_d['max_cost'])) |
             (Q(min_cost_of_sale__lte=mm_d['min_cost']) & Q(max_cost_of_sale__gte=mm_d['max_cost']))) &
            Q(is_group_multiple_objs=True) |

            (Q(cost_of_sale__gte=mm_d['min_cost']) & Q(cost_of_sale__lte=mm_d['max_cost']))
        )
    elif 'min_cost' in mm_d and 'max_cost' not in mm_d:
        params.append(
            (Q(min_cost_of_sale__gte=mm_d['min_cost']) | Q(max_cost_of_sale__gte=mm_d['min_cost'])) &
            Q(is_group_multiple_objs=True) |

            Q(cost_of_sale__gte=mm_d['min_cost'])
        )
    elif 'min_cost' not in mm_d and 'max_cost' in mm_d:
        params.append(
            (Q(min_cost_of_sale__lte=mm_d['max_cost']) | Q(max_cost_of_sale__lte=mm_d['max_cost'])) &
            Q(is_group_multiple_objs=True) |

            Q(cost_of_sale__lte=mm_d['max_cost'])
        )

    print('params =>', params)
    print('mm_d =>', mm_d)

    queryset = queryset \
        .filter(*params) \
        .extra(select=select, order_by=order_by)

    return queryset
