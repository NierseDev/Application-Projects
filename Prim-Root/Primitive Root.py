def is_prime(q):
    if q <= 1:
        return False
    for i in range(2, int(q**0.5) + 1):
        if q % i == 0:
            return False
    return True

def is_primitive_root(g, q):
    """
    Check if g is a primitive root of q.

    Args:
        g (int): The number to check.
        q (int): The prime number.

    Returns:
        bool: True if g is a primitive root of q, False otherwise.
    """
    seen = set()
    for i in range(1, q):
        result = pow(g, i, q)
        if result in seen:
            return False
        seen.add(result)
        if result == 1:
            return i == q - 1
    return False

def find_primitive_roots(q):
    """
    Find all primitive roots of q.

    Args:
        q (int): The prime number.

    Returns:
        list: A list of primitive roots of q.
    """
    roots = []
    for g in range(1, q):
        if is_primitive_root(g, q):
            roots.append(g)
    return roots

def check_primitive_root(q, g):
    """
    Check if g is a primitive root of q and print the results.

    Args:
        q (int): The prime number.
        g (int): The number to check.
    """
    if not is_prime(q):
        print(f"{q} is not a prime number!!")
        return
    print(f"{q}:")
    for i in range(1, q):
        results = []
        for j in range(1, q):
            result = pow(i, j, q)
            results.append(f"{i}^{j} mod {q} = {result}")
            if result == 1:
                break
        result_str = ", ".join(results)
        if is_primitive_root(i, q):
            print(f"{result_str} ==> {i} is primitive root of {q}")
        else:
            print(result_str)
    roots = find_primitive_roots(q)
    print(f"{g} is primitive root: {is_primitive_root(g, q)} [{', '.join(map(str, roots))}]")

# Test the function
q = 12
g = 5
check_primitive_root(q, g)