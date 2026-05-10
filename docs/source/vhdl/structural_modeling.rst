Structural Modeling
===================

Structural modeling is a way of describing a digital system by connecting together pre-defined components. It is analogous to creating a schematic by placing chips and drawing wires between them.

-----------------------
Component Declaration
-----------------------

To use a module inside another module, you must first declare it as a **component** in the architecture's declarative region (before the `begin` keyword).

.. code-block:: vhdl

   architecture Structural of TopModule is
       component SubModule
           port (
               a : in  std_logic;
               b : out std_logic
           );
       end component;
       
       signal internal_wire : std_logic;
   begin
       -- Instantiation goes here
   end architecture;

-----------------------
Component Instantiation
-----------------------

You create an instance of the component using the `port map` statement. There are two ways to map signals:

**1. Positional Mapping** (Discouraged)
Maps signals based on their order in the component declaration.

.. code-block:: vhdl

   u1: SubModule port map (sig_a, sig_b);

**2. Named Mapping** (Recommended)
Maps signals explicitly by name. This is much safer and more readable.

.. code-block:: vhdl

   u1: SubModule port map (
       a => sig_a,
       b => sig_b
   );

-----------------------
Direct Instantiation (VHDL-93 and later)
-----------------------

In modern VHDL, you can instantiate an entity directly without declaring a component first. This reduces boilerplate code.

.. code-block:: vhdl

   u1: entity work.SubModule
       port map (
           a => sig_a,
           b => sig_b
       );

-----------------------
The `Generate` Statement
-----------------------

If you need to instantiate multiple identical components (e.g., an 8-bit register made of 8 flip-flops), use the `for...generate` loop.

.. code-block:: vhdl

   gen_label: for i in 0 to 7 generate
       ff_inst: entity work.D_FlipFlop
           port map (
               clk => clk,
               d   => input_bus(i),
               q   => output_bus(i)
           );
   end generate;

-----------------------
Configurations
-----------------------

A **Configuration** is a VHDL construct used to specify which architecture should be used for each component instance in a design. While powerful, configurations are less commonly used in modern FPGA design, where direct instantiation or default architecture binding is preferred.

Next, we will cover **Generics** and parameterized designs.
