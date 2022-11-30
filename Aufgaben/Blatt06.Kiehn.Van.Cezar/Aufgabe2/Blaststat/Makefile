.PHONY:test
test:test_values test_distrib test_corrupt
	@echo "Congratulations: $@ passed"

.PHONY:test_values
test_values:
	@./blaststat.py blaststat.txt | grep '^V' | diff - blaststat_values.tsv
	@echo "Congratulations: $@ passed"

.PHONY:test_distrib
test_distrib:
	@./blaststat.py blaststat.txt | grep '^[#D]' | diff - blaststat_distrib.tsv
	@echo "Congratulations: $@ passed"

.PHONY:test_corrupt
test_corrupt:
	@./blaststat.py blaststat_corrupt.txt | diff - emptyfile.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_error
test_error:
	@./check_err.py
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__ 
