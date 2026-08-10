.PHONY: srpm

srpm:
	dnf install -y rpmdevtools rpm-build
	spectool --get-files --directory $(dir $(spec)) $(spec)
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(dir $(spec))" \
		--define "_srcrpmdir $(outdir)"
