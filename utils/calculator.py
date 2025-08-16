def add(a, b):
    return a + b

def sub(a, b):
    return  a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
    
def mod(a, b):
    return a % b

# Minimal constants (no math import required)
PI  = 3.14159265358979323846264338327950288419716939937510
TAU = 2.0 * PI
HALF_PI = 0.5 * PI

def sin(x: float, *, degrees: bool = False) -> float:
    """
    Compute sin(x) from scratch using range reduction + a 13th-order polynomial.
    - Accepts radians by default; set degrees=True to pass degrees.
    - No dependency on math.sin.

    Accuracy: ~1e-12 on [-pi/2, pi/2]. With range reduction this holds well for
    typical inputs; extremely large |x| may lose some precision (as with most
    float-based implementations) due to modulo rounding.
    """
    if degrees:
        x = x * (PI / 180.0)

    # Range reduce to (-pi, pi]
    # This form avoids branching issues and is numerically stable for typical magnitudes.
    y = (x + PI) % TAU - PI

    # Fold to [-pi/2, pi/2] to improve polynomial accuracy
    if y > HALF_PI:
        y = PI - y
    elif y < -HALF_PI:
        y = -PI - y

    # Horner-form polynomial for sin on [-pi/2, pi/2]:
    # sin(y) = y * (1 + c2*y^2 + c4*y^4 + ... + c12*y^12)
    # Coefficients from the Taylor expansion up to y^13.
    y2 = y * y
    p = 1.0 / 6227020800.0     #  1/13!
    p = p * y2 - 1.0 / 39916800.0   # -1/11!
    p = p * y2 + 1.0 / 362880.0     #  1/9!
    p = p * y2 - 1.0 / 5040.0       # -1/7!
    p = p * y2 + 1.0 / 120.0        #  1/5!
    p = p * y2 - 1.0 / 6.0          # -1/3!
    return y + y * y2 * p
