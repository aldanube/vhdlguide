Packages and Subprograms
========================

VHDL provides subprograms (Functions and Procedures) and Packages to organize code, improve readability, and promote reuse.

-----------------------
Functions
-----------------------

A **Function** is a subprogram that takes input parameters and returns a single value. Functions are always combinational and execute in zero simulation time.

.. code-block:: vhdl

   function Add_Numbers(a, b : integer) return integer is
   begin
       return a + b;
   end function;

Functions can be called from within concurrent statements or processes.

-----------------------
Procedures
-----------------------

A **Procedure** can have multiple input, output, and inout parameters. Unlike functions, procedures can contain `wait` statements, which means they can model sequential behavior over time (useful in testbenches).

.. code-block:: vhdl

   procedure Toggle_Signal(signal s : inout std_logic; constant delay : time) is
   begin
       s <= not s;
       wait for delay;
       s <= not s;
   end procedure;

-----------------------
Packages
-----------------------

A **Package** is used to group related declarations (types, constants, components, subprograms) into a single reusable unit.

A package consists of two parts:
1. **Package Declaration**: Defines the public interface.
2. **Package Body**: Contains the implementation of subprograms.

.. code-block:: vhdl

   -- Package Declaration
   package MyProject_Pkg is
       constant DATA_WIDTH : integer := 32;
       type data_array is array (natural range <>) of std_logic_vector(DATA_WIDTH-1 downto 0);
       function Calculate_Parity(v : std_logic_vector) return std_logic;
   end package;

   -- Package Body
   package body MyProject_Pkg is
       function Calculate_Parity(v : std_logic_vector) return std_logic is
           variable parity : std_logic := '0';
       begin
           for i in v'range loop
               parity := parity xor v(i);
           end loop;
           return parity;
       end function;
   end package body;

-----------------------
Using a Package
-----------------------

To use a package in your design, include it at the top of your VHDL file.

.. code-block:: vhdl

   use work.MyProject_Pkg.all;

-----------------------
Standard Packages
-----------------------

- **`std_logic_1164`**: Basic logic types.
- **`numeric_std`**: Arithmetic for signed and unsigned vectors.
- **`textio`**: File I/O for simulation.

Next, we will look at **VHDL-2008** features.
