Basic Design Structure
======================

A VHDL design is composed of several key elements that define the interface and the internal logic of a module. The three main components are **Libraries**, **Entities**, and **Architectures**.

-----------------------
1. Libraries and Packages
-----------------------

Before defining an entity, you must declare the libraries and packages you intend to use. The most common library is `IEEE`, which contains the standard logic types.

.. code-block:: vhdl

   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;
   use IEEE.NUMERIC_STD.ALL; -- For arithmetic operations

-----------------------
2. The Entity
-----------------------

The **Entity** defines the external interface of the module. It specifies the input and output ports.

.. code-block:: vhdl

   entity AND_Gate is
       Port (
           A : in  std_logic;
           B : in  std_logic;
           Y : out std_logic
       );
   end entity AND_Gate;

-----------------------
3. The Architecture
-----------------------

The **Architecture** defines the internal logic or behavior of the module. Every entity must have at least one architecture associated with it.

.. code-block:: vhdl

   architecture Behavioral of AND_Gate is
   begin
       Y <= A and B;
   end architecture Behavioral;

-----------------------
Putting it All Together
-----------------------

Here is a complete VHDL file for a simple 2-input AND gate:

.. code-block:: vhdl

   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;

   entity AND_Gate is
       Port (
           A : in  std_logic;
           B : in  std_logic;
           Y : out std_logic
       );
   end entity AND_Gate;

   architecture Behavioral of AND_Gate is
   begin
       Y <= A and B;
   end architecture Behavioral;

-----------------------
Design Separation
-----------------------

VHDL strictly separates the **interface** (Entity) from the **implementation** (Architecture). This allows you to have multiple implementations (e.g., behavioral, structural, or post-synthesis) for the same interface without changing the modules that instantiate it.

Next, we will cover **Data Types** in VHDL.
