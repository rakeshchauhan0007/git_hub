weight = int(input('weight of the person :'))
name = input('name of person:')
weight_in_kg_lb = input('pounds(p) or kg(k):')
kg= weight/2.205
pounds = kg * 2.205
if weight_in_kg_lb.lower() == 'p':
    pounds = weight * 2.205
    print(f'converting {weight} kg of {name} weight  in to pounds {pounds}')
elif weight_in_kg_lb.upper() == 'K':
    kg = weight / 2.205
    print(f'converting  {weight} pounds of {name} weight into {kg} kg')
else:
    print('please, provide some appropriate information')