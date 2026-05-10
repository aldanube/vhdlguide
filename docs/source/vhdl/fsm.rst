Finite State Machines (FSMs)
============================

Finite State Machines are the heart of control logic in digital systems. In VHDL, FSMs are typically implemented using a combination of an `enumeration` type and one or more processes.

-----------------------
Types of FSMs
-----------------------

1. **Moore Machine**: The outputs depend only on the current state.
2. **Mealy Machine**: The outputs depend on both the current state and the current inputs.

-----------------------
The Recommended Two-Process Style
-----------------------

A clean way to implement an FSM is to use two processes: one for the **state register** (sequential) and one for the **next state logic and outputs** (combinational).

.. code-block:: vhdl

   -- 1. Define the states
   type state_type is (IDLE, START, PROCESSING, DONE);
   signal current_state, next_state : state_type;

   -- 2. State Register Process (Sequential)
   process (clk, reset)
   begin
       if reset = '1' then
           current_state <= IDLE;
       elsif rising_edge(clk) then
           current_state <= next_state;
       end if;
   end process;

   -- 3. Next State and Output Logic (Combinational)
   process (current_state, input_signal)
   begin
       -- Default values
       next_state <= current_state;
       output_signal <= '0';

       case current_state is
           when IDLE =>
               if input_signal = '1' then
                   next_state <= START;
               end if;

           when START =>
               output_signal <= '1';
               next_state <= PROCESSING;

           when PROCESSING =>
               -- logic here
               next_state <= DONE;

           when DONE =>
               next_state <= IDLE;
       end case;
   end process;

-----------------------
One-Process Style
-----------------------

Alternatively, you can implement the entire FSM in a single sequential process. This can be more compact but sometimes makes output timing (e.g., registered outputs) harder to visualize.

-----------------------
FSM Encoding
-----------------------

Synthesis tools can automatically choose the best encoding (Binary, One-hot, Gray) for your FSM. You can often provide hints to the compiler using attributes like `fsm_encoding`.

-----------------------
Best Practices
-----------------------

- Use **enumeration types** for state names rather than constants/integers for better readability and debugging.
- Always handle the **`when others`** case in a `case` statement, even if you think you've covered all states.
- Keep output logic simple to avoid long combinational paths.

Next, we will cover **Testbenches and Simulation**.

-----------------------
Credits
-----------------------

Maintained and authored by **Agus L. Setiawan**. For more FPGA guides, visit `Technolati.com <https://www.technolati.com/>`_.

