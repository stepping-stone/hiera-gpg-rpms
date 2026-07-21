srpm:
	dnf install -y spectool rpmbuild
	spectool -g -R rubygem-gpgme.spec
	rpmbuild -bs rubygem-gpgme.spec --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)"
