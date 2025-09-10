
def Recidivism_score(prior_arrests,prior_arrests_local_ordinance,age):
    score = 0
    if age>=40:
        score-=1
    elif age<=24 and age>=18:
        score +=1
    if prior_arrests >=5:
        score+=2
    elif prior_arrests >=2:
        score+=1
    if prior_arrests_local_ordinance == 'Y':
        score+=1
    print(f'The recidivism risk score is {score}')
user_pa = int(input('Prior arrest: '))
user_palo = input('Prior arrest for local ordinance (Y/N): ')
user_aar = int(input('Age at release: '))
Recidivism_score(user_pa,user_palo,user_aar)
