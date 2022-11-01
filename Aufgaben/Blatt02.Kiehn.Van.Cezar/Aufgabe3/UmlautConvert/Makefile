.PHONY:test

.PHONY:to_utf8
to_utf8:post_an_den_zwiebelfisch_latex.txt
	@./umlaut_latex_to_utf8.py $< | diff - post_an_den_zwiebelfisch_utf8.txt
	@echo "Congratulations: $@ passed"

.PHONY:to_latex
to_latex:post_an_den_zwiebelfisch_utf8.txt
	@./umlaut_utf8_to_latex.py $< | diff - post_an_den_zwiebelfisch_latex.txt
	@echo "Congratulations: $@ passed"

test:to_utf8 to_latex
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@echo "nothing to be cleaned"
