srpm:
	dnf install -y spectool rpmbuild
	spectool -g -R rubygem-optimist.spec
	rpmbuild -bs rubygem-optimist.spec --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)"
