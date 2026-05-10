Sequential Logic and the Process Statement
==========================================

In VHDL, sequential logic is implemented using the **`process`** statement. While VHDL as a whole is concurrent, the statements inside a process are executed sequentially from top to bottom.

-----------------------
The Process Statement
-----------------------

A process is triggered whenever one of the signals in its **sensitivity list** changes value.

.. code-block:: vhdl

   process (clk, reset)
   begin
       -- Sequential logic goes here
   end process;

-----------------------
Synchronous Logic (Flip-Flops)
-----------------------

To create synchronous hardware, we check for a clock edge using the `rising_edge()` function or the `'event` attribute.

.. code-block:: vhdl

   process (clk)
   begin
       if rising_edge(clk) then
           q <= d; -- Simple D-Flip-Flop
       end if;
   end process;

-----------------------
Asynchronous Reset
-----------------------

An asynchronous reset is included in the sensitivity list and checked before the clock edge.

.. code-block:: vhdl

   process (clk, reset)
   begin
       if reset = '1' then
           q <= '0';
       elsif rising_edge(clk) then
           q <= d;
       end if;
   end process;

-----------------------
Signals vs. Variables
-----------------------

Inside a process, you can use both **Signals** and **Variables**:

- **Signals (`<=`)**: Updated only after the process finishes execution. They represent physical wires and registers.
- **Variables (`:=`)**: Updated immediately. They are local to the process and are used for temporary calculations.

.. code-block:: vhdl

   process (clk)
       variable temp : integer := 0;
   begin
       if rising_edge(clk) then
           temp := temp + 1; -- Updated immediately
           counter <= temp;  -- Signal updated after process
       end if;
   end process;

-----------------------
Inferred Latches
-----------------------

A common mistake in VHDL is unintentionally inferring a **latch**. This happens when a signal is not assigned a value in every possible execution path of a process.

.. warning::
   To avoid latches, ensure all `if` statements have an `else` clause, or provide a default value at the beginning of the process.

Next, we will discuss **Combinational Logic**.
