.PHONY:test
test:
	@./celsius.py | diff - celsius_out.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
