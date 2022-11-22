.PHONY:test
TARGET=scatter_plot.pdf
.PHONY:plot.pdf

${TARGET}:coords.tsv
	@./plot_coords.py $< && test -f ${TARGET}

test:${TARGET}
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} ${TARGET}
