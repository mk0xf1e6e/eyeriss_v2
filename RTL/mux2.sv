/*
* mux2.sv
* 2-to-1 multiplexer
* Author : Milad Karami
* Date   : 2025-01-10
*/

module mux2 #(
  parameter int WIDTH = 16
) (
  input  [WIDTH-1:0] in0,  // input 0
  input  [WIDTH-1:0] in1,  // input 1
  input              sel,  // select signal
  output [WIDTH-1:0] out   // output
);
  // if sel is 1, then out = in1, otherwise out = in0
  assign out = sel ? in1 : in0;
endmodule
