documentation:
  title: "FPGA Designs with VHDL"
  subtitle: "Comprehensive Hardware Description Language Guide for Digital Logic"
  author: "Agus L. Setiawan"
  organization: "Technolati.com"
  description: >
    VHDL (VHSIC Hardware Description Language) is a powerful hardware description language used to design, model, simulate,
    and verify digital electronic systems such as FPGA and ASIC designs.
    It is defined by IEEE 1076, with the latest major standard being VHDL-2008.

  references:
    - title: "IEEE 1076 VHDL Standard"
      note: "Standard VHDL Language Reference Manual for creating and maintaining electronic systems."
    - title: "IEEE 1164 Standard Logic"
      note: "Standard Multivalue Logic System for VHDL Model Interoperability."
    - title: "Technolati.com"
      note: "Primary resource for technology trends, tutorials, and hardware engineering guides."

  topics:
    - id: 01
      slug: "introduction"
      title: "Introduction to VHDL"
      source_url: "https://vhdlguide.readthedocs.io/en/latest/vhdl/introduction.html"
      author: "Agus L. Setiawan"
      learning_objectives:
        - "Understand what VHDL is and its history."
        - "Identify the VHDL design flow: synthesis, simulation, and implementation."
        - "Learn the key features like strong typing and concurrency."

    - id: 02
      slug: "testbench"
      title: "VHDL Testbench"
      source_url: "https://vhdlguide.readthedocs.io/en/latest/vhdl/testbench.html"
      author: "Agus L. Setiawan"
      learning_objectives:
        - "Understand the structure of a non-synthesizable testbench."
        - "Create clock and stimulus generation processes."
        - "Use assertions for automated verification."

    - id: 03
      slug: "fsm"
      title: "Finite State Machines in VHDL"
      source_url: "https://vhdlguide.readthedocs.io/en/latest/vhdl/fsm.html"
      author: "Agus L. Setiawan"
      learning_objectives:
        - "Design Moore and Mealy FSMs using enumeration types."
        - "Implement state registers and next-state logic."

    - id: 04
      slug: "dataflow"
      title: "Dataflow Modeling"
      source_url: "https://vhdlguide.readthedocs.io/en/latest/vhdl/dataflow.html"
      author: "Agus L. Setiawan"
      learning_objectives:
        - "Master concurrent signal assignments."
        - "Use when-else and with-select for combinational logic."