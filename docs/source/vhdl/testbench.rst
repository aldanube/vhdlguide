Testbenches and Simulation
==========================

A testbench is a VHDL module used to verify the functionality of another module (the Design Under Test or DUT). Testbenches are not synthesizable; they are only used for simulation.

-----------------------
Structure of a Testbench
-----------------------

A testbench has no ports in its entity. It instantiates the DUT and provides stimulus to its inputs.

.. code-block:: vhdl

   entity TB_MyDesign is
   end entity TB_MyDesign;

   architecture Stimulus of TB_MyDesign is
       -- 1. Component declaration for DUT
       component MyDesign
           Port ( clk, rst, d : in std_logic; q : out std_logic );
       end component;

       -- 2. Local signals to connect to DUT
       signal clk_tb : std_logic := '0';
       signal rst_tb : std_logic := '0';
       signal d_tb   : std_logic := '0';
       signal q_tb   : std_logic;

       -- 3. Clock period definition
       constant CLK_PERIOD : time := 10 ns;

   begin
       -- 4. Instantiate the DUT
       uut: MyDesign port map (
           clk => clk_tb,
           rst => rst_tb,
           d   => d_tb,
           q   => q_tb
       );

       -- 5. Clock generation process
       clk_process : process
       begin
           clk_tb <= '0';
           wait for CLK_PERIOD/2;
           clk_tb <= '1';
           wait for CLK_PERIOD/2;
       end process;

       -- 6. Stimulus process
       stim_proc: process
       begin
           rst_tb <= '1';
           wait for 20 ns;
           rst_tb <= '0';
           
           d_tb <= '1';
           wait for 20 ns;
           
           d_tb <= '0';
           wait for 20 ns;

           -- End simulation
           wait;
       end process;
   end architecture;

-----------------------
Assertions and Reporting
-----------------------

Use the `assert` statement to check for expected values and `report` to print messages to the simulator console.

.. code-block:: vhdl

   assert (q_tb = expected_val)
   report "Error: Output q does not match expected value!"
   severity error;

-----------------------
Wait Statements
-----------------------

In testbenches, `wait` statements are used to control time:

- `wait for 10 ns;`: Pauses for a specific time.
- `wait until rising_edge(clk);`: Waits for a specific condition.
- `wait;`: Pauses indefinitely (used at the end of a stimulus process).

-----------------------
File I/O
-----------------------

VHDL provides the `TEXTIO` package for reading input data from a file or writing simulation results to a file. This is useful for large-scale verification with pre-generated test vectors.

Next, we will look at **Structural Modeling** and component instantiation.

-----------------------
Credits
-----------------------

This verification guide was created by **Agus L. Setiawan** for `Technolati.com <https://www.technolati.com/>`_.

