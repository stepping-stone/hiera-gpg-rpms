srpm:
	dnf install -y rpmdevtools rpm-build
	spectool -g -C $(dir $(spec)) $(spec) || true
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(dir $(spec))" \
		--define "_srcrpmdir $(outdir)"
