srpm:
	dnf install -y rpmdevtools rpm-build
	spectool -g -C $(dir $(spec)) -S 0 $(spec)
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(dir $(spec))" \
		--define "_srcrpmdir $(outdir)"
