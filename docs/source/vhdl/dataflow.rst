Dataflow Modeling
=================

Dataflow modeling in VHDL describes a system in terms of how data flows through it from inputs to outputs using concurrent signal assignments. This is often the most concise way to describe simple combinational logic.

-----------------------
Concurrent Signal Assignments
-----------------------

Unlike sequential statements inside a process, concurrent statements are evaluated in parallel. They are always "active" and respond immediately to any change in their input signals.

.. code-block:: vhdl

   -- Simple dataflow assignment
   Y <= A and B;

-----------------------
Conditional Signal Assignment
-----------------------

The `when-else` statement is a common dataflow construct used to model multiplexers and conditional logic.

.. code-block:: vhdl

   -- 2-to-1 MUX
   Y <= A when (sel = '1') else B;

-----------------------
Selected Signal Assignment
-----------------------

The `with-select` statement is used when an assignment depends on multiple values of a single expression.

.. code-block:: vhdl

   -- 4-to-1 MUX
   with sel select
       Y <= A when "00",
            B when "01",
            C when "10",
            D when others;

-----------------------
Dataflow vs. Behavioral
-----------------------

- **Dataflow**: Describes the logic using Boolean equations and concurrent statements. It is usually closer to the physical gate-level structure.
- **Behavioral**: Describes *what* the module does using sequential algorithms inside a process. It is more abstract and easier to read for complex logic.

-----------------------
When to Use Dataflow
-----------------------

Dataflow modeling is ideal for:
- Simple logic gates and decoders.
- Bus multiplexing and routing.
- Continuous assignments that don't require complex state-based logic.

By using dataflow modeling, you can write code that is both readable and highly efficient for synthesis tools.

-----------------------
Credits
-----------------------

This tutorial is part of the VHDL Design Series by **Agus L. Setiawan**, supported by `Technolati.com <https://www.technolati.com/>`_.

