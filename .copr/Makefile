srpm:
	dnf install -y rpm-build
	cd $(dir $(spec)) && \
		curl -L -O $(shell rpm --eval "%{expand:$(shell grep '^Source' $(spec) | head -1 | awk '{print $$2}')}")
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(dir $(spec))" \
		--define "_srcrpmdir $(outdir)"
