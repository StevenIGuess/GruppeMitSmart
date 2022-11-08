.PHONY:test
test:
	@./hydrocount.py proteins.txt | diff - proteins_hydrocount.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
