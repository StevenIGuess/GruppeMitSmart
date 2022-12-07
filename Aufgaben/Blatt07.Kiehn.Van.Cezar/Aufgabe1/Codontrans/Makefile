.PHONY:test
test:
	@./cds2protein.py ZNF148_cds.txt | diff - ZNF148_protein.txt
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
