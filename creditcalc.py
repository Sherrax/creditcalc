import argparse
import math
def main():

    parser = argparse.ArgumentParser(description="Kalkulator kredytowy")
    parser.add_argument("--principal", type=float, help="")
    parser.add_argument("--periods", type=int, help="")
    parser.add_argument("--interest", type=float, help="")
    parser.add_argument("--payment", type=float, help="")
    parser.add_argument("--type", type=str, help="")
    args = parser.parse_args()
    #data_analysis(args)
    print(check_non_negative(args))
def data_analysis(args):
    if args.interest and check_non_negative(args):
        if not args.payment and args.type == 'annuity':
            calculating_the_monthly_payment(args.principal, args.periods, args.interest)
        elif not args.principal and args.type == 'annuity':
            calculating_the_loan_principal(args.payment,args.periods,args.interest)
        elif not args.periods and args.type == 'annuity':
            number_of_monthly_payments(args.principal,args.payment,args.interest)
        elif not args.payment and args.type == 'diff':
            calculating_differentiated_payments(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters 2")
    else:
        print("Incorrect parameters 1")





def monthly_payment( value):
    print('Enter the number of months:')
    months = float(input())
    payments = math.ceil(value / months)
    lastpaymant = value - (months - 1) * payments

    if payments == lastpaymant:
        print('Your monthly payment = {}'.format(int(lastpaymant)))
    else:
        print('Your monthly payment = {} and the last payment = {}.'.format(int(payments),int(lastpaymant)))

def number_of_monthly_payments(principal,payment,interest):

    i = interest/(12 * 100)
    n = math.ceil(math.log(payment/(payment - i * principal),1+i))
    months = n%12
    year = int(n/12)
    overpayment = math.ceil(n * payment - principal)
    if (months ==0):
        print('It will take {} years to repay this loan!\nOverpayment ={}'.format(year,overpayment))
    else:
        print('It will take {} years and {} months to repay this loan!\nOverpayment ={}'.format(year,months,overpayment))

def calculating_the_monthly_payment(principal,periods,interest):
    i = interest / (12 * 100)
    a = math.ceil(principal * (i * math.pow(i +1,periods))/((math.pow(i +1,periods)) -1))
    overpayment = math.ceil(a * periods - principal)
    print('Your annuity payment = {}!\nOverpayment ={}'.format(a,overpayment))

def calculating_the_loan_principal(payment,periods,interest):
    i = interest / (12 * 100)
    k = math.pow(1 + i,periods)
    p = int(payment/((i *k)/(k-1)))
    overpayment = math.ceil(periods * payment - p)
    print('Your loan principal = {}!\nOverpayment = {}'.format(p,overpayment))


def calculating_differentiated_payments(principal,periods,interest):
    P =principal
    n = periods
    i = interest/1200
    m = 1
    k =0

    while m <= n:
        D = P/n + i * (P - (P*(m-1))/(n))
        print('Month {}: payment is {}'.format(m,math.ceil(D)))
        m +=1
        k +=math.ceil(D)

    print('\nOverpaiment = ' + str(int(k - principal)))

def check_non_negative(args):
    for arg in vars(args):
        value = getattr(args, arg)
        if isinstance(value, (int,float)) and value < 0:
            return False
    return True

main()