Design Examples and Exercises (DEX)
===================================

This section provides practical design examples and exercises to help you master VHDL design concepts.

-----------------------
Example 1: 4-bit Binary Counter
-----------------------

A simple synchronous counter with asynchronous reset and enable.

.. code-block:: vhdl

   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;
   use IEEE.NUMERIC_STD.ALL;

   entity Counter_4bit is
       Port (
           clk   : in  std_logic;
           rst   : in  std_logic;
           en    : in  std_logic;
           count : out std_logic_vector(3 downto 0)
       );
   end entity;

   architecture Behavioral of Counter_4bit is
       signal r_count : unsigned(3 downto 0) := (others => '0');
   begin
       process(clk, rst)
       begin
           if rst = '1' then
               r_count <= (others => '0');
           elsif rising_edge(clk) then
               if en = '1' then
                   r_count <= r_count + 1;
               end if;
           end if;
       end process;
       count <= std_logic_vector(r_count);
   end architecture;

-----------------------
Example 2: 7-Segment Decoder
-----------------------

A combinational logic block that converts a 4-bit nibble into the segments for a common-cathode 7-segment display.

.. code-block:: vhdl

   -- Implementation using 'with-select'
   with nibble select
       segments <= "1111110" when "0000", -- 0
                   "0110000" when "0001", -- 1
                   "1101101" when "0010", -- 2
                   -- ... and so on
                   "0000000" when others;

-----------------------
Exercises
-----------------------

1. **Shift Register**: Create an 8-bit shift register that can shift left or right based on a control signal.
2. **PWM Generator**: Design a Pulse Width Modulation generator with a 4-bit duty cycle input.
3. **Sequence Detector**: Implement an FSM that detects the sequence "1101" in a serial bit stream.

-----------------------
Next Steps
-----------------------

After practicing these examples, you can move on to the **Advanced VHDL** sections to learn about structural modeling and generics.
