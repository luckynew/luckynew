

##################################################
######How many month do you need to##################
######save enough money for the down payment###########

####part1: salary without growth######
##annual_salary = int( input( 'Enter your annual salary: ' ))
##portion_saved = float( input( 'Enter the percent of your  salary to save, as a decimal: ' ) )
##total_cost = int( input( 'Enter the cost of your dream home:' ) )
##portion_down_payment = total_cost * 0.25
##current_saving = 0.0
##r = 0.04
##i = 0
##while current_saving < portion_down_payment :
##    current_saving  +=( annual_salary*portion_saved + current_saving * r )/12
##    i += 1
##print( i )

##part2: salary with growth######
##annual_salary = int( input( 'Enter your annual salary: ' ))
##portion_saved = float( input( 'Enter the percent of your  salary to save, as a decimal: ' ) )
##total_cost = int( input( 'Enter the cost of your dream home:' ) )
##semi_annual_raise = float( input( 'Enter the semiannual raise, as a decimal: ') )
##portion_down_payment = total_cost * 0.25
##current_saving = 0.0
##r = 0.04
##i = 0
##while current_saving < portion_down_payment :
##    current_saving  += ( annual_salary*portion_saved + current_saving * r )/12
##    if i % 6 == 0 and i !=0 :
##        annual_salary  = annual_salary *( 1+ semi_annual_raise)
##    i += 1
##print( i )
##print( 'years: ', i//12,' ; ', 'month: ', i %12)

####part3: how many months ######
annual_salary =  int( input( ' Enter the starting salary: ' ))
##portion_saved = #float( input( 'Enter the percent of your  salary to save, as a decimal: ' ) )
total_cost = 1000000 #int( input( 'Enter the cost of your dream home:' ) )
semi_annual_raise = .07#float( input( 'Enter the semiannual raise, as a decimal: ') )
portion_down_payment = total_cost * 0.25
epsilon = 100
current_saving = 0.0
r = 0.04
guess_number = 0
low = 0
high =10000
guess = 0

def saving( annual_salary1, guess1 ):
    current_saving = 0.0
    for i in range(0, 36 ):
        current_saving  += ( annual_salary1*float(guess1/10000) + current_saving * r )/12
        if i % 6 == 0 and i !=0 :
            annual_salary1  = annual_salary1 *( 1.+ semi_annual_raise)
    return current_saving

if saving(annual_salary, 10000 ) < portion_down_payment:
    print('It is not possible to pay the down payment in 36 months!' )
    
while abs( saving(annual_salary, guess) - portion_down_payment ) > epsilon:
    guess = ( low + high ) / 2
    if saving(annual_salary, guess) < portion_down_payment:
        low = guess
    else:
        high = guess
    guess_number += 1
print(  ' Best saving rate:' , float(guess/10000) , '\n',  'Steps in bisection:', guess_number )





