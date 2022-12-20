.PHONY:test

test:test_encode test_decode

.PHONY:test_encode
test_encode:
	@./morseClass.py SOS
	@./morseClass.py morse_wiki.txt
	@./morseClass.py --text morse_wiki.txt | diff - morse_wiki.code
	@./morseClass.py --mc2_0 --text morse_wiki.txt | diff - morse_wiki.code2_0
	@echo "Congratulations: $@ passed"

.PHONY:test_sound
test_sound:
	@./morseClass.py Congratulations | sh -s

.PHONY:test_sound_MS_WINDOWS
test_sound_MS_WINDOWS:
	@./morseClass.py --MS_WINDOWS SOS

.PHONY:test_decode
test_decode:
	@./morseClass.py -d morse_wiki.code2_0 | diff -i - morse_wiki.txt
	@./morseClass.py -d unknown_short.code2_0 | ./morseClass.py --mc2_0 --text - | diff - unknown_short.code2_0
	@./morseClass.py -d unknown.code2_0 | ./morseClass.py --mc2_0 --text - | diff - unknown.code2_0
	@echo "Congratulations: $@ passed"

.PHONY:clean
clean:
	@${RM} -r __pycache__

