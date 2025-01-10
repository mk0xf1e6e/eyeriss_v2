module mux2 (
	in0,
	in1,
	sel,
	out
);
	parameter signed [31:0] WIDTH = 16;
	input [WIDTH - 1:0] in0;
	input [WIDTH - 1:0] in1;
	input sel;
	output wire [WIDTH - 1:0] out;
	assign out = (sel ? in1 : in0);
endmodule
