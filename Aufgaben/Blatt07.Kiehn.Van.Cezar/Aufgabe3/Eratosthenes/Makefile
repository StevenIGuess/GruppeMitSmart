.PHONY:test
test:test_small test_medium test_large test_huge
	@echo "Congratulations: $@ passed"

.PHONY:test_small
test_small:
	@./eratosthenes.py 20 | diff - prime_list_20.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_medium
test_medium:
	@./eratosthenes.py 200 | diff - prime_list_200.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_large
test_large:
	@./eratosthenes.py 1000 | diff - prime_list_1000.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_huge
test_huge:
	@./eratosthenes.py 10000 | diff - prime_list_10000.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
