^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package heron_control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

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
