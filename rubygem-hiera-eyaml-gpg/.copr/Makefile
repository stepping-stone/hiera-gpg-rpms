srpm:
	dnf install -y spectool rpmbuild
	spectool -g -R rubygem-hiera-eyaml-gpg.spec
	rpmbuild -bs rubygem-hiera-eyaml-gpg.spec --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)"
