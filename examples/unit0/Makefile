default: precision rounding_control

precision: precision.cpp
	g++ $< -o $@

rounding_control: rounding_control.cpp
	g++ $< -o $@

clean:
	$(RM) precision rounding_control

.SUFFIXES:
.PHONY: default clean
