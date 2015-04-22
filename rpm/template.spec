Name:           ros-indigo-mico-description
Version:        0.0.22
Release:        0%{?dist}
Summary:        ROS mico_description package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin

%description
3D Model and URDF of the Kinova MICO Arm

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Apr 22 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.22-0
- Autogenerated by Bloom

* Fri Apr 17 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.21-0
- Autogenerated by Bloom

* Tue Apr 14 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.20-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.19-0
- Autogenerated by Bloom

* Fri Apr 03 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.18-0
- Autogenerated by Bloom

* Fri Mar 27 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.17-0
- Autogenerated by Bloom

* Tue Mar 24 2015 Mathijs de Langen <langen@robot-rose.nl> - 0.0.16-0
- Autogenerated by Bloom

