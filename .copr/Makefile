srpm:
	dnf install -y rpmdevtools rpm-build
	spectool -g -C $(dir $(spec)) $(spec) || true
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(dir $(spec))" \
		--define "_srcrpmdir $(outdir)" \
		--nodeps \
		--define "_build_arch x86_64" \
		--define "_arch x86_64"
