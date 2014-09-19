Name:           ros-indigo-wpi-jaco-wrapper
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS wpi_jaco_wrapper package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/wpi_jaco_wrapper
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-ecl-geometry
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-jaco-sdk
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-wpi-jaco-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-ecl-geometry
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-jaco-sdk
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-wpi-jaco-msgs

%description
ROS Wrapper for the JACO Arm Developed at WPI

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Sep 19 2014 David Kent <davidkent@wpi.edu> - 0.0.7-0
- Autogenerated by Bloom

* Tue Sep 02 2014 David Kent <davidkent@wpi.edu> - 0.0.6-0
- Autogenerated by Bloom

* Mon Aug 25 2014 David Kent <davidkent@wpi.edu> - 0.0.5-0
- Autogenerated by Bloom

