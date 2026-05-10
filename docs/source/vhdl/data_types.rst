VHDL Data Types and Operators
=============================

VHDL is a **strongly typed** language. This means that you cannot perform operations between different types without explicit conversion. This rigor helps catch design errors early in the process.

-----------------------
The `std_logic` System
-----------------------

Defined in the `IEEE.STD_LOGIC_1164` package, `std_logic` is the standard type for modeling digital signals. Unlike a simple bit (0 or 1), `std_logic` can have 9 different values, representing various hardware states:

- `'U'`: Uninitialized
- `'X'`: Forcing Unknown (Conflict)
- `'0'`: Forcing Low
- `'1'`: Forcing High
- `'Z'`: High Impedance (Tri-state)
- `'W'`: Weak Unknown
- `'L'`: Weak Low
- `'H'`: Weak High
- `'-'`: Don't care

For synthesis, `'0'`, `'1'`, and `'Z'` are the most critical.

-----------------------
Common Scalar Types
-----------------------

- **`std_logic`**: A single wire/signal.
- **`boolean`**: Can be `true` or `false`.
- **`integer`**: A whole number. Standard integers are 32-bit.
- **`bit`**: A single bit (0 or 1), but less flexible than `std_logic`.

-----------------------
Vector Types (Arrays)
-----------------------

- **`std_logic_vector`**: An array of `std_logic` elements. Used for buses and registers.

.. code-block:: vhdl

   signal data_bus : std_logic_vector(7 downto 0); -- 8-bit bus

- **`signed` / `unsigned`**: Vectors used for arithmetic. Defined in `IEEE.NUMERIC_STD`.

.. code-block:: vhdl

   signal count : unsigned(3 downto 0); -- 4-bit counter

-----------------------
Operators
-----------------------

VHDL provides a variety of operators:

- **Logical**: `and`, `or`, `nand`, `nor`, `xor`, `xnor`, `not`.
- **Relational**: `=`, `/=`, `<`, `<=`, `>`, `>=`.
- **Arithmetic**: `+`, `-`, `*`, `/`, `mod`, `rem`. (Note: `/`, `mod`, `rem` are often not synthesizable for arbitrary values).
- **Shift**: `sll`, `srl`, `sla`, `sra`, `rol`, `ror`.
- **Concatenation**: `&` (Used to combine signals into a vector).

.. code-block:: vhdl

   combined_sig <= bit_a & bit_b & bus_c;

-----------------------
Type Casting
-----------------------

Because of strong typing, you must often cast between types, especially when using `numeric_std`:

.. code-block:: vhdl

   -- Convert unsigned to std_logic_vector
   output_bus <= std_logic_vector(my_unsigned_sig);

   -- Convert integer to unsigned
   my_unsigned_sig <= to_unsigned(15, 4); -- Value 15, width 4

Next, we will look at **Sequential Logic** and the `process` statement.
