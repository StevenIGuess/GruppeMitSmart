.PHONY:test
FILES=hypo.tsv nothypo.tsv locus.tsv ranges.tsv

.PHONY:${FILES}

islands_nohead.tsv:islands_nohead.sh islands.tsv
	@sh ./islands_nohead.sh > $@
	@diff $@ islands_nohead_solution.tsv
	@echo "Congratulations: $< passed"

hypo.tsv:hypo.sh islands_nohead.tsv
	@sh ./hypo.sh > $@
	@diff $@ hypo_solution.tsv
	@echo "Congratulations: $< passed"

nothypo.tsv:nothypo.sh islands_nohead.tsv
	@sh ./nothypo.sh > $@
	@diff $@ nothypo_solution.tsv
	@echo "Congratulations: $< passed"

locus.tsv:locus.sh islands_nohead.tsv
	@sh ./locus.sh > $@
	@diff $@ locus_solution.tsv
	@echo "Congratulations: $< passed"

ranges.tsv:ranges.sh islands_nohead.tsv
	@sh ./ranges.sh > $@
	@diff $@ ranges_solution.tsv
	@echo "Congratulations: $< passed"

test:islands_nohead.tsv ${FILES}
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	${RM} ${FILES} islands_nohead.tsv
