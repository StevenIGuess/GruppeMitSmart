.PHONY:test
test:test2 test4 test7 test4_7 test1_9 test_err

.PHONY:test2
test2:
	$(eval TMPFILE := $(shell mktemp))
	@head -n 2 skyline1-9.txt | tail -n 1 > ${TMPFILE}
	@./skyline.py 2 | diff - ${TMPFILE}
	@echo "Congratulations: $@ passed"

.PHONY:test4
test4:
	$(eval TMPFILE := $(shell mktemp))
	@head -n 4 skyline1-9.txt | tail -n 1 > ${TMPFILE}
	@./skyline.py 4 | diff - ${TMPFILE}
	@echo "Congratulations: $@ passed"

.PHONY:test7
test7:
	$(eval TMPFILE := $(shell mktemp))
	@head -n 7 skyline1-9.txt | tail -n 1 > ${TMPFILE}
	@./skyline.py 7 | diff - ${TMPFILE}
	@echo "Congratulations: $@ passed"

.PHONY:test4_7
test4_7:
	$(eval TMPFILE := $(shell mktemp))
	@head -n 7 skyline1-9.txt | tail -n 4 > ${TMPFILE}
	@./skyline.py 4 7 | diff - ${TMPFILE}
	@echo "Congratulations: $@ passed"

.PHONY:test1_9
test1_9:
	@./skyline.py 1 9 | diff - skyline1-9.txt
	@echo "Congratulations: $@ passed"

.PHONY:test_err
test_err:
	./check_err.py

.PHONY:clean
clean:
	@${RM} -r __pycache__
