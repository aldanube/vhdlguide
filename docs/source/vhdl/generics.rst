Generics and Parameterized Designs
==================================

Generics allow you to create flexible, reusable VHDL modules by parameterizing constants such as bus widths, delay times, or initial values.

-----------------------
Defining Generics
-----------------------

Generics are defined in the **Entity** block, before the `Port` declaration.

.. code-block:: vhdl

   entity N_Bit_Counter is
       generic (
           WIDTH : integer := 8 -- Default width is 8 bits
       );
       port (
           clk   : in  std_logic;
           count : out unsigned(WIDTH-1 downto 0)
       );
   end entity;

-----------------------
Using Generics in Logic
-----------------------

The generic value can be used throughout the architecture to define signal widths, loop ranges, or constants.

.. code-block:: vhdl

   architecture Behavioral of N_Bit_Counter is
       signal internal_count : unsigned(WIDTH-1 downto 0) := (others => '0');
   begin
       process(clk)
       begin
           if rising_edge(clk) then
               internal_count <= internal_count + 1;
           end if;
       end process;
       count <= internal_count;
   end architecture;

-----------------------
Overriding Generics during Instantiation
-----------------------

When you instantiate a module, you can override its default generic values using the `generic map` statement.

.. code-block:: vhdl

   u1: entity work.N_Bit_Counter
       generic map (
           WIDTH => 16 -- Override default width to 16 bits
       )
       port map (
           clk   => main_clk,
           count => bus_16bit
       );

-----------------------
Common Uses for Generics
-----------------------

- **Bus Widths**: Making modules work with 8, 16, 32, or 64-bit data.
- **Clock Frequencies**: Passing timing information for internal baud rate generators.
- **Memory Sizes**: Defining the depth and width of RAM or FIFO blocks.
- **Simulation Delays**: Including timing parameters that are only active during simulation.

-----------------------
Generics vs. Constants
-----------------------

While constants are fixed within a package or architecture, generics are passed down from a higher-level module. This makes generics the preferred way to create truly "library" style components.

Next, we will discuss **Packages and Subprograms**.
