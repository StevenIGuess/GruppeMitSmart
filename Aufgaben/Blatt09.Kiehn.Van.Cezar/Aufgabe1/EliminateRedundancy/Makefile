.PHONY:
test:
	@./structured.py | diff - result.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
