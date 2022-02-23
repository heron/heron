^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package heron_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.4.0 (2022-02-23)
------------------

0.3.5 (2022-02-23)
------------------
* Squashed commit of the following:
  commit 51454398314997a7bb04571e8e73d3072ccc618d
  Author: Chris Iverach-Brereton <civerachb@clearpathrobotics.com>
  Date:   Fri Oct 29 16:46:01 2021 -0400
  Add a teleop.launch file and a default gamepad configuration (copied from Jackal) to allow easier teleop in gazebo
  commit d9c7af570d5af7679f46b5633481541a223af8bf
  Author: Chris Iverach-Brereton <civerachb@clearpathrobotics.com>
  Date:   Thu Aug 5 12:08:19 2021 -0400
  Add an empty config file + the HERON_CONFIG_EXTRAS envar, same as on the Husky.
  commit 51fa5b444eb2298f68aaea98bae7ba2b751b51d4
  Author: Chris Iverach-Brereton <civerachb@clearpathrobotics.com>
  Date:   Fri Feb 12 11:55:41 2021 -0500
  0.3.4
  commit 7521812ddbfcf6ee75012f86924d4a4248bb0352
  Author: Chris Iverach-Brereton <civerachb@clearpathrobotics.com>
  Date:   Fri Feb 12 11:47:21 2021 -0500
  Update changelogs ahead of release
  commit 125cb786bf4b4eee358b276bb45f1e62731d7587
  Author: Chris I-B <59611394+civerachb-cpr@users.noreply.github.com>
  Date:   Tue Feb 2 16:02:29 2021 -0500
  Fix disconnected thruster joints (`#12 <https://github.com/heron/heron/issues/12>`_)
  * Use a fixed joint for the thrusters unless we're in simulation; these joints are purely decorative outside gazebo, and the tf is not published except in simulation anyway
  * Remove superfluous .py; they were a copy & paste error
  commit f7db9cee55c8b7ba3be1d90f5e240b392cee5348
  Merge: b592e3e 2766fea
  Author: Tony Baltovski <tbaltovski@clearpathrobotics.com>
  Date:   Mon Feb 1 12:43:48 2021 -0800
  Merge pull request `#11 <https://github.com/heron/heron/issues/11>`_ from heron/no-um6
  Rename UM6 env vars to be generic IMU
  commit 2766fea3525a4a5b15eae440efe2376a84fbcde9
  Author: Chris Iverach-Brereton <civerachb@clearpathrobotics.com>
  Date:   Mon Feb 1 15:20:27 2021 -0500
  Rename the UM6 IMU env vars to remove the reference to UM6; make them generic IMU vars instead
  commit b592e3ee121ba10d19a223663770764a5690e215
  Author: Tony Baltovski <tbaltovski@clearpathrobotics.com>
  Date:   Thu Sep 17 10:50:09 2020 -0400
  [heron_description] Dropped --in-order arg from xacro since it is default in Melodic.
  commit 5bca3d45d4a1a45d5d774feed70aaf84fad574d8
  Author: Tony Baltovski <tbaltovski@clearpathrobotics.com>
  Date:   Thu Sep 17 10:48:16 2020 -0400
  [heron_description] Added xacro xml namespace prefix.
  commit e7685347065b02a23724fdbbff1f1ffa0187f7ad
  Author: Tony Baltovski <tbaltovski@clearpathrobotics.com>
  Date:   Thu Sep 17 10:45:54 2020 -0400
  [heron_description] Dropped .py on xacro since it is deprecated.
  commit 6d960f37f92b505cfc5d8431fe85157decfbe171
  Author: Tony Baltovski <tbaltovski@clearpathrobotics.com>
  Date:   Thu Sep 17 10:17:29 2020 -0400
  0.3.3
  commit 78ed21de3491c9b3177b6aa33f9d32c001c4b56a
  Author: Tony Baltovski <tbaltovski@clearpathrobotics.com>
  Date:   Thu Sep 17 10:17:17 2020 -0400
  Changes.
* Update ROS deps to remove/rename third-party packages that are not available on Melodic
* Merge pull request `#10 <https://github.com/heron/heron/issues/10>`_ from heron/interactive_ring_fix
  Change the topic the gazebo mag plugin publishes to
* Related to https://github.com/heron/heron_simulator/pull/6.  Change the topic that the mag data is published to so we can translate it to the new message standard to work-around a bug with the imu filter.
* Contributors: Chris I-B, Chris Iverach-Brereton

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
