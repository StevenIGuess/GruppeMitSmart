.PHONY:test

test:test10 test_err
	@echo "Congratulations: $@ passed"

.PHONY:test10
test10:
	@./zahlenreihen.py 10 | diff - zahlenreihenk10.txt
	@echo "Congratulations: $@ passed"

test_err:
	@./check_err.py ./zahlenreihen.py
	@echo "Congratulations: $@ passed"

.PHONE:clean
clean:
	@${RM} -r __pycache__
