weight = int(input('weight of the person :'))
weight_in_kg_lb = input('pounds(p) or kg(k):')
kg= weight/2.205
pounds = kg * 2.205
if weight_in_kg_lb == 'p':
    pounds = weight * 2.205
    print(f'converting {weight} kg to pounds {pounds}')

else:
    kg = weight / 2.205
    print(f'converting  {weight} pounds into {kg} kg')