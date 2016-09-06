Name:           mysqld_exporter   
Version:        0.8.0
Release:        1%{?dist}
Summary:        mysqld_exporter for prometheus
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        mysqld_exporter
Source1:        mysqld_exporter.service
Source2:        mysqld_exporter.default
License:        GPL


%description
Prometheus Exporter for mysqld metrics 

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system/
mkdir -p $RPM_BUILD_ROOT/etc/default/
install -m 755 %{_sourcedir}/mysqld_exporter $RPM_BUILD_ROOT/usr/bin
install -m 644 %{_sourcedir}/mysqld_exporter.service $RPM_BUILD_ROOT/lib/systemd/system/
cp %{_sourcedir}/mysqld_exporter.default $RPM_BUILD_ROOT/etc/default/mysqld_exporter 

%files
/lib/systemd/system/mysqld_exporter.service
/usr/bin/mysqld_exporter
%attr(0640,mysql,mysql) /etc/default/mysqld_exporter

%doc



%changelog
