.PHONY:test

test:test_small test_large

.PHONY:test_small
test_small:forbidden_functions.sh
	@./data_matrix_class.py -s '	' -k H He Li -a atomicNumber symbol name meltingPoint -o atom-data.tsv | sort > atom-data-tmp.tsv
	@sort atom-data-mini.tsv | diff -w - atom-data-tmp.tsv
	@rm -f atom-data-tmp.tsv
	@./forbidden_functions.sh
	@echo "Congratulations: $@ passed"

.PHONY:test_large
test_large:forbidden_functions.sh
	@./data_matrix_class.py -s '	' -o  atom-data.tsv | sort > atom-data-tmp.tsv
	@sort atom-data.tsv | diff - atom-data-tmp.tsv
	@rm -f atom-data-tmp.tsv
	@./forbidden_functions.sh
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
