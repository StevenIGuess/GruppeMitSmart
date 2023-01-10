.PHONY:test
test:unittest progtest errortest

.PHONY:unittest
unittest:
	@./pwgen_unit_test.py
	@echo "Congratulations: $@ passed"

.PHONY:progtest
progtest:
	@./pwgen.py | head -n 1 | diff - head1_default.txt
	@./pwgen.py -n 5 | head -n 1 | diff - head1_default.txt
	@./pwgen.py -n 5 | tail -n 5 | wc -c | diff -w - tail_count_cc.txt
	@./pwgen.py -s w3d2p2w4 | head -n 1 | diff - head1_w3d2p2w4.txt
	@./pwgen.py -n 10 -s w3d2p2w4 | tail -n 10 | wc -c | diff -w - tail_count_cc.txt
	@echo "Congratulations: $@ passed"

.PHONY:errortest
errortest:
	@./check_err.py
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
