.PHONY:test
test:	
	@./convert_dates.py chronik_der_BRD_orig.txt | diff - chronik_der_BRD_tt.mm.yyyy.txt
	@echo "Congratulations. $@ passed"

.PHONY:clean
clean:
	@echo "nix zu tun"
