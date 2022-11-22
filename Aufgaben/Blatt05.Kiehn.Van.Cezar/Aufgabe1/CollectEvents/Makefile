.PHONY:test
test:test_small test_large

.PHONY:test_small
test_small:
	@./collect_events.py events_first20.txt | diff - re_match_counts_first20.tsv
	@echo "Congratulations. $@ passed"

.PHONY:test_large
test_large:
	@./collect_events.py events.txt | diff - re_match_counts.tsv
	@echo "Congratulations. $@ passed"
