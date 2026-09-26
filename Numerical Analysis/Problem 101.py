def u(n):
    """Generates the terms of the 10th-degree polynomial sequence:
    u_n = 1 - n + n^2 - n^3 + n^4 - n^5 + n^6 - n^7 + n^8 - n^9 + n^10
    """
    return sum((-1)**i * (n**i) for i in range(11))

def solve_linear_system(A, b):
    """Solves the linear system A * x = b using Gaussian elimination with partial pivoting."""
    n = len(b)
    # Create an augmented matrix
    M = [A[i] + [b[i]] for i in range(n)]
    
    for i in range(n):
        # Partial pivoting for numerical stability
        max_row = i
        for r in range(i + 1, n):
            if abs(M[r][i]) > abs(M[max_row][i]):
                max_row = r
        M[i], M[max_row] = M[max_row], M[i]
        
        # Forward elimination
        for r in range(i + 1, n):
            factor = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= factor * M[i][c]
                
    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for c in range(i + 1, n):
            x[i] -= M[i][c] * x[c]
        x[i] /= M[i][i]
        
    return x

def solve_project_euler_101():
    total_fit_sum = 0
    
    # For a 10th-degree polynomial sequence, k ranges from 1 to 10.
    for k in range(1, 11):
        x_vals = [i for i in range(1, k + 1)]
        y_vals = [float(u(i)) for i in range(1, k + 1)]
        
        # 1. Construct the Vandermonde matrix A and vector b for the system
        # Row format: [1, x, x^2, ..., x^{k-1}]
        A = [[x**j for j in range(k)] for x in x_vals]
        b = y_vals
        
        # 2. Calculate the full equation system using custom Gaussian elimination
        coefficients = solve_linear_system(A, b)
        
        # 3. Calculate the First Incorrect Term (FIT) at n = k + 1
        next_x = k + 1
        fit_val = sum(c * (next_x**j) for j, c in enumerate(coefficients))
        
        total_fit_sum += round(fit_val)
        
    return total_fit_sum

if __name__ == "__main__":
    result = solve_project_euler_101()
    print(f"The sum of FITs for the bad optimal polynomials is: {result}")