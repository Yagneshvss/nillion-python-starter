from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # perform the multiplication of my_int1 and my_int2
    multiplication_result = my_int1 * my_int2
    
    # perform the subtraction of my_int2 from the multiplication result
    final_result = multiplication_result - my_int2

    return [Output(final_result, "my_output", party1)]
