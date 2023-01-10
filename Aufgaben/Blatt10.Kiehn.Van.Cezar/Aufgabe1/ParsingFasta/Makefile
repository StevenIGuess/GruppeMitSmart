.PHONY:test
test:
	@./fnarw.py | diff - sample_translated.fa
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
