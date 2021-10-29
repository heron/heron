^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package heron_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.4 (2021-02-12)
------------------
* Fix disconnected thruster joints (`#12 <https://github.com/heron/heron/issues/12>`_)
  * Use a fixed joint for the thrusters unless we're in simulation; these joints are purely decorative outside gazebo, and the tf is not published except in simulation anyway
  * Remove superfluous .py; they were a copy & paste error
* Merge pull request `#11 <https://github.com/heron/heron/issues/11>`_ from heron/no-um6
  Rename UM6 env vars to be generic IMU
* Rename the UM6 IMU env vars to remove the reference to UM6; make them generic IMU vars instead
* [heron_description] Dropped --in-order arg from xacro since it is default in Melodic.
* [heron_description] Added xacro xml namespace prefix.
* [heron_description] Dropped .py on xacro since it is deprecated.
* Contributors: Chris Iverach-Brereton, Tony Baltovski

0.3.3 (2020-09-17)
------------------
* Update ROS deps to remove/rename third-party packages that are not available on Melodic
* Related to https://github.com/heron/heron_simulator/pull/6.  Change the topic that the mag data is published to so we can translate it to the new message standard to work-around a bug with the imu filter.
* Contributors: Chris Iverach-Brereton

0.3.2 (2020-01-24)
------------------
* Changed mesh declarations to use packages instead of xacro finds (`#8 <https://github.com/heron/heron/issues/8>`_)
* Contributors: Dave Niewinski

0.3.1 (2019-04-18)
------------------
* changed plugin names in xacro files. (`#7 <https://github.com/heron/heron/issues/7>`_)
* Uploaded propeller.dae
  * Put in some missing dependencies and upgraded package.xml to format 2.0
  * Uploaded propeller model
* Put in some missing dependencies and upgraded package.xml to format 2.0 (`#5 <https://github.com/heron/heron/issues/5>`_)
* Fixed Heron accessories glitch with custom namespaces
* Merge pull request `#2 <https://github.com/heron/heron/issues/2>`_ from Nirzvi1/kinetic-devel
  Added heron_control, changed heron_description to use with uuv_simulator
* Removed heron_msgs dependency and added roslaunch back
* Fixing namespaces to allow for empty namespace
* Added simpler collision mesh
* Fixed spacing using Atom auto-indent
* Undoing package number changes
* Further implementing namespaces
* Renamed navsat/vel topic to allow Vec3->Twist translation
* Added envvars to change sensor locations and attached GPS info to separate sensor frame
* Made changes to allow the actual Heron robot to use heron_description
* Removed uuv_msgs dependencies (not actually needed)
* Changed simulated GPS topic to match the actual topic
* Additional updates so Gazebo sensor plugins would work with namespaces
* Re-added copyright notice in heron.urdf.xacro
* Switched UUV Sensor plugins to Gazebo plugins
* Updated version in package.xml
* Initial commit of new heron_description files
* Contributors: Guy Stoppi, Shreya Subramaniam, Tony Baltovski

0.3.0 (2018-04-12)
------------------
* Updated gps and imu default locations for next version of heron
* Updated stls and xacro definitions for kinetic syntax changes
* Contributors: Dave Niewinski

0.2.3 (2018-04-12)
------------------
* Added missing sonar link.
* Added Ceepulse sonar accessory.
* Contributors: Administrator, Tony Baltovski

0.2.2 (2016-08-03)
------------------
* Updated the UM6 orientation.
* Added lms1xx as run dependency.
* Contributors: Tony Baltovski

0.2.1 (2016-07-08)
------------------
* Updated meshes and added rear plate.
* Contributors: Tony Baltovski

0.2.0 (2016-07-06)
------------------
* Updated the UM6 orientation.
* Added SICK lms1xx laser and Axis ptz camera to accessories.
* Added Power message.
* Added optional Novatel Smart6 GPS, updated Gazebo GPS plugin and made default environment variables more specific.
* Fixed IMU angle substitution.
* Updated URDF.
* Heron rename.
* Contributors: Tony Baltovski

0.1.0 (2014-12-02)
------------------
* Add roslaunch file check to kingfisher_description.
* Contributors: Mike Purvis

0.0.4 (2014-03-05)
------------------
* fix the launch arg name
* unnecessary xacro sonar xacro file
* adding sonar to a seperate urdf, and to description launch
* add gps to standard sensor suite
* Contributors: Yan Ma

0.0.3 (2013-10-24)
------------------

0.0.2 (2013-10-15)
------------------
* Fix model colours, retab base file.
* Basic catkinization of description package.
* Move kingfisher_description into subdirectory.
