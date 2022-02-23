^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package heron_control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.5 (2022-02-23)
------------------
* Apply the modified EKF configuration to fix the odom frame drifting (`#17 <https://github.com/heron/heron/issues/17>`_)
  * Apply the modified EKF configuration to fix the odom frame drifting
  * Remove the z velocity
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
* Add a teleop.launch file and a default gamepad configuration (copied from Jackal) to allow easier teleop in gazebo
* Contributors: Chris I-B, Chris Iverach-Brereton

0.3.4 (2021-02-12)
------------------

0.3.3 (2020-09-17)
------------------

0.3.2 (2020-01-24)
------------------
* [heron_control] Fixing missing dep and minor clean-up.
* Contributors: Tony Baltovski

0.3.1 (2019-04-18)
------------------
* Put in some missing dependencies and upgraded package.xml to format 2.0 (`#5 <https://github.com/heron/heron/issues/5>`_)
* Merge pull request `#2 <https://github.com/heron/heron/issues/2>`_ from Nirzvi1/kinetic-devel
  Added heron_control, changed heron_description to use with uuv_simulator
* Merge branch 'kinetic-devel' into kinetic-devel
* Fixing mistake from rebasing
* Made global covariance accessible from navsat/fix callback
* Allowed use of odometry yaw for simulation
* Fixed name+email in copyright notices
* Removed NWU->ENU swapping because it's only needed for simulation
* Put covariance-adding script into heron_control pkg
* Fixed robot_localization to expect TwistWithCovarianceStamped for navsat/vel
* Added heron_control package (`#1 <https://github.com/heron/heron/issues/1>`_)
  * Added heron_control package
  * Deleted unnecessary comments from CMakeLists.txt
  * Updated robot_localization.yaml
  Deleted unnecessary comments
  Set frequency to 20Hz (the default update frequency of the um6 IMU).
  * Edited package.xml and moved heron_controller node from heron_control
  * Updated package.xml description
* Added navsat/vel to robot_localization.yaml
* Removed initial slash to allow for namespace prefixing
* Updated package.xml description
* Edited package.xml and moved heron_controller node from heron_control
* Updated robot_localization.yaml
  Deleted unnecessary comments
  Set frequency to 20Hz (the default update frequency of the um6 IMU).
* Deleted unnecessary comments from CMakeLists.txt
* Added functionality of GPS datum via env var
* Merge pull request `#3 <https://github.com/heron/heron/issues/3>`_ from Nirzvi1/kinetic-devel-datum
  Added functionality of GPS datum via env var
* Added functionality of GPS datum via env var
* Added heron_control package (`#1 <https://github.com/heron/heron/issues/1>`_)
  * Added heron_control package
  * Deleted unnecessary comments from CMakeLists.txt
  * Updated robot_localization.yaml
  Deleted unnecessary comments
  Set frequency to 20Hz (the default update frequency of the um6 IMU).
  * Edited package.xml and moved heron_controller node from heron_control
  * Updated package.xml description
* Added heron_control package
* Contributors: Guy Stoppi, Nirzvi1, Tony Baltovski
