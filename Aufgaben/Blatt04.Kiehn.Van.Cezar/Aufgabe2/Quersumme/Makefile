.PHONY:test
test:test_positive test_err
	@echo "Congratulations: $@ passed"

.PHONY:test_positive
test_positive:
	@./run.sh | diff - quersummen.tsv
	@echo "Congratulations: $@ passed"

.PHONY:test_err
test_err:
	@./check_err.py
	@echo "Congratulations: $@ passed"

.PHONE:clean
clean:
	@${RM} -r __pycache__
