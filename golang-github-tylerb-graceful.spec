#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-tylerb-graceful
Version  : 9a3d4236b03bb5d26f7951134d248f9d5510d599
Release  : 5
URL      : https://github.com/tylerb/graceful/archive/9a3d4236b03bb5d26f7951134d248f9d5510d599.tar.gz
Source0  : https://github.com/tylerb/graceful/archive/9a3d4236b03bb5d26f7951134d248f9d5510d599.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-googlecode-go-net

%description
graceful [![GoDoc](https://godoc.org/github.com/tylerb/graceful?status.png)](http://godoc.org/github.com/tylerb/graceful) [![Build Status](https://drone.io/github.com/tylerb/graceful/status.png)](https://drone.io/github.com/tylerb/graceful/latest) [![Coverage Status](https://coveralls.io/repos/tylerb/graceful/badge.svg?branch=dronedebug)](https://coveralls.io/r/tylerb/graceful?branch=dronedebug) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/tylerb/graceful?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
========

%prep
%setup -q -n graceful-9a3d4236b03bb5d26f7951134d248f9d5510d599

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/tylerb/graceful"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/tylerb/graceful || :

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/tylerb/graceful/graceful.go
/usr/lib/golang/src/github.com/tylerb/graceful/graceful_test.go
/usr/lib/golang/src/github.com/tylerb/graceful/tests/main.go
