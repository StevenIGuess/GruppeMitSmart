.PHONY:test
FILES=references.tsv \
       aligned_only.tsv \
       references_count.tsv

FILES_ADVANCED=reads_n_alignments.tsv\
               reads_n_alignments.sh aligned_only.tsv

.PHONY:${FILES}

references.tsv:references.sh alignments.sam
	@sh ./references.sh > $@
	@diff $@ references_solution.tsv
	@echo "Congratulations: $< passed"

aligned_only.tsv:aligned_only.sh alignments.sam references.tsv
	@sh ./aligned_only.sh > $@
	@diff $@ aligned_only_solution.tsv
	@echo "Congratulations: $< passed"

references_count.tsv:references_count.sh alignments.sam
	@sh ./references_count.sh > $@
	@diff -w $@ references_count_solution.tsv
	@echo "Congratulations: $< passed"

test:${FILES}
	@echo "Congratulations: $@ passed"

reads_n_alignments.tsv:reads_n_alignments.sh aligned_only.tsv
	@sh ./reads_n_alignments.sh > $@
	@diff $@ reads_n_alignments_solution.tsv
	@echo "Congratulations: $< passed"

reads_n_alignments_distri.tsv:reads_n_alignments_distri.sh reads_n_alignments.tsv
	@sh ./reads_n_alignments_distri.sh > $@
	@diff $@ reads_n_alignments_distri_solution.tsv
	@echo "Congratulations: $< passed"

test_advanced:${FILES_ADVANCED}
	@echo "Congratulations: $@ passed"

clean:
	${RM} ${FILES} ${FILES_ADVANCED}
