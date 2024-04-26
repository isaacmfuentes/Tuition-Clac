import argparse
import sys

def calculate_tuition(credits=12, resident=True, dt=False):
    if credits < 0:
        raise ValueError("Credits must be non-negative.")
    
    flat_tuition_md = 4412.00
    flat_tuition_non_md = 17468.00
    per_credit_md = 367.00
    per_credit_non_md = 1456.00
    differential_tuition_flat = 1428.00
    differential_tuition_per_credit = 118.00
    fee_9_or_more = 977.50
    fee_1_to_8 = 455.00
    
    if credits == 0:
        return 0.00
    
    if credits >= 12:
        if resident:
            tuition = flat_tuition_md
        else:
            tuition = flat_tuition_non_md
        if dt:
            tuition += differential_tuition_flat
    else:
        if resident:
            tuition = credits * per_credit_md
        else:
            tuition = credits * per_credit_non_md
        if dt:
            tuition += credits * differential_tuition_per_credit
    
    if credits >= 9:
        fees = fee_9_or_more
    else:
        fees = fee_1_to_8
    
    return tuition + fees

def parse_args(arglist):
    parser = argparse.ArgumentParser(description="Calculate UMD tuition and fees.")
    parser.add_argument("-c", "--credits", type=int, default=12, help="Number of credits")
    parser.add_argument("-nr", "--nonresident", action="store_true", help="Non-resident status")
    parser.add_argument("-dt", "--differentialtuition", action="store_true", help="Differential tuition")
    
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    resident = not args.nonresident  
    tuition_and_fees = calculate_tuition(args.credits, resident, args.differentialtuition)
    print(f"Your tuition and fees total ${tuition_and_fees:.2f}")
