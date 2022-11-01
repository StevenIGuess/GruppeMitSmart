.PHONY:test
test:
	@./leapyear.py 1800 1900 2000 2004 2017 | diff - leapyear_out.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
