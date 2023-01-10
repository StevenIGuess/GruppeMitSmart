.PHONY:test
test:
	@./predictionqual.py --gold_standard goldstandard.tsv prediction[0-9]*.tsv | diff - quality_out.tsv
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__
