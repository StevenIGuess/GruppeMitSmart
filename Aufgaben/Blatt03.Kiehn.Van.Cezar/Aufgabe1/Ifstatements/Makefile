.PHONY:test
test:
	@${RM} numbers.txt
	@touch numbers.txt
	@for num in 1 2 3 4 5 6; do\
	  echo $$num >> numbers.txt;\
	done
	@./true_statements.py | diff - numbers.txt
	@${RM} numbers.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
