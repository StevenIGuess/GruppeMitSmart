.PHONY:test
test:test_P1_fold50 test_fold70 test_fold60 test_fold50
	@echo "Congratulations: $@ passed"

.PHONY:test_P1_fold50
test_P1_fold50:
	@./fold_text.py 50 python_history_P1.txt | diff - python_history_P1_fold50.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_fold70
test_fold70:
	@./fold_text.py 70 python_history.txt | diff - python_history_fold70.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_fold60
test_fold60:
	@./fold_text.py 60 python_history.txt | diff - python_history_fold60.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_fold50
test_fold50:
	@./fold_text.py 50 python_history.txt | diff - python_history_fold50.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
