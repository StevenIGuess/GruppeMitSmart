.PHONY:test
test:test1 test2 test3 test4
	@echo "Congratulations: $@ passed"

.PHONY:test1
test1:
	@./gen_email.py patient1.tsv email_generisch.txt | diff - email1.txt
	@echo "Congratulations: $@ passed"

.PHONY:test2
test2:
	@./gen_email.py patient2.tsv email_generisch.txt | diff - email2.txt
	@echo "Congratulations: $@ passed"

.PHONY:test3
test3:
	@./gen_email.py patient3.tsv email_generisch.txt | diff - email3.txt
	@echo "Congratulations: $@ passed"

.PHONY:test4
test4:
	@./gen_email.py patient4.tsv email_generisch.txt | diff - email4.txt
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
