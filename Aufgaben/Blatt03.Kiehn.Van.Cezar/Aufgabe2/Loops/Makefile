.PHONY:test
test:
	@./loops.py | diff - loops-out.txt
	@echo "Congratulations: $@ passed"

.PHONE:clean
clean:
	@${RM} -r __pycache__
