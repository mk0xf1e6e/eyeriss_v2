import os
import random
import cocotb

from cocotb.triggers import Timer
from cocotb.runner import get_runner

# The width of mul
WIDTH = 16

@cocotb.test()
async def test_mux2(dut):
  """ Testing the multiplexer with 2 inputs and 1 output

  Args:
      dut (cocotb.handle.SimHandle): handle to the DUT
  """

  # Number of test vectors
  n_tests = 100

  # Running the test
  for _ in range(n_tests):
    # Random inputs
    in0 = random.randint(0, 2**WIDTH - 1)
    in1 = random.randint(0, 2**WIDTH - 1)
    sel = random.randint(0, 1)
    # Setting the inputs
    dut.in0 <= in0
    dut.in1 <= in1
    dut.sel <= sel
    # Waiting for the output
    await Timer(1, units="ns")
    # Getting the output
    out = int(dut.out.value.binstr, 2)
    # Checking the output
    if sel == 0:
      assert dut.out == in0, f"mux2: {in0}, {in1}, {sel}, {out}"
    else:
      assert dut.out == in1, f"mux2: {in0}, {in1}, {sel}, {out}"
    # If the test passes, print the inputs and the output
    print(f"PASSED: {in0}, {in1}, {sel}, {out}")

if __name__ == "__main__":
  # First getting the sim
  sim = os.getenv("SIM", "verilator")
  # Project path
  proj_path = os.path.join(os.path.dirname(__file__), "..")
  # Getting the source files of verilog
  sources = os.listdir(os.path.join(proj_path, "verilog"))
  sources = [os.path.join(proj_path, "verilog", source) for source in sources]

  # Running the test
  runner = get_runner(sim)
  runner.build(
      sources=sources,
      # Top level HDL module
      hdl_toplevel="mux2",
      clean=True,
      verbose=False,
      # Add your parameters here
      parameters={
          "WIDTH": WIDTH,
      },
      # Set this to True if you want to see the waveform
      waves=True,
  )

  runner.test(
      # Top level HDL module
      hdl_toplevel="mux2",
      # Name of the test module (cocotb)
      test_module="test_mux2",
      verbose=False,
      # Set this to True if you want to see the waveform
      waves=True,
  )
