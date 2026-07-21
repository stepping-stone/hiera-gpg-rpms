srpm:
	dnf install -y spectool rpmbuild
	spectool -g -R rubygem-hiera-eyaml.spec
	rpmbuild -bs rubygem-hiera-eyaml.spec --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)"
