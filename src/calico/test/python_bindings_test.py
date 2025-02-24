import calico.calico_native as calico_native

import numpy as np
import unittest

class TestCalicoPythonBindings(unittest.TestCase):

    def test_Pose3d(self):
        expected_rot = [-0.774982, -0.1549964, -0.2324946, 0.5668556]
        expected_pos = [1.5, 2.3, 6.8]
        temp_pose = calico_native.Pose3d()
        temp_pose.rotation = expected_rot
        temp_pose.translation = expected_pos
        np.testing.assert_allclose(temp_pose.rotation, np.array(expected_rot), 1e-7)
        np.testing.assert_equal(temp_pose.translation, np.array(expected_pos))

    def test_Accelerometer(self):
        accelerometer = calico_native.Accelerometer()
        # Set/get name.
        test_name = 'test'
        accelerometer.SetName(test_name)
        self.assertEqual(test_name, accelerometer.GetName())
        # Set/get model.
        test_model = (
            calico_native.AccelerometerIntrinsicsModel.kAccelerometerScaleOnly)
        self.assertTrue(accelerometer.SetModel(test_model).ok())
        self.assertEqual(test_model, accelerometer.GetModel())
        # Set/get intrinsics.
        test_intrinsics = [1]
        accelerometer.SetIntrinsics(test_intrinsics)
        np.testing.assert_equal(test_intrinsics, accelerometer.GetIntrinsics())
        # Set/get extrinsics.
        test_extrinsics = calico_native.Pose3d()
        test_extrinsics.rotation = [-0.774982, -0.1549964, -0.2324946, 0.5668556]
        test_extrinsics.translation = [1.5, 2.3, 6.8]
        accelerometer.SetExtrinsics(test_extrinsics)
        actual_extrinsics = accelerometer.GetExtrinsics()
        np.testing.assert_allclose(test_extrinsics.rotation,
                                   actual_extrinsics.rotation, 1e-7)
        np.testing.assert_equal(test_extrinsics.translation, actual_extrinsics.translation)
        # Set/get latency.
        test_latency = 0.02
        self.assertTrue(accelerometer.SetLatency(test_latency).ok())
        self.assertEqual(test_latency, accelerometer.GetLatency())
        # Add measurements.
        measurement = calico_native.AccelerometerMeasurement()
        measurement.id.stamp = 0
        measurement.id.sequence = 0
        self.assertTrue(accelerometer.AddMeasurement(measurement).ok())
        measurements = []
        for i in range(3):
            new_measurement = calico_native.AccelerometerMeasurement()
            new_measurement.id.stamp = i + 1
            new_measurement.id.sequence = i + 1
            measurements.append(new_measurement)
        self.assertTrue(accelerometer.AddMeasurements(measurements).ok())
        
    def test_Gyroscope(self):
        gyroscope = calico_native.Gyroscope()
        # Set/get name.
        test_name = 'test'
        gyroscope.SetName(test_name)
        self.assertEqual(test_name, gyroscope.GetName())
        # Set/get model.
        test_model = (
            calico_native.GyroscopeIntrinsicsModel.kGyroscopeScaleOnly)
        self.assertTrue(gyroscope.SetModel(test_model).ok())
        self.assertEqual(test_model, gyroscope.GetModel())
        # Set/get intrinsics.
        test_intrinsics = [1]
        gyroscope.SetIntrinsics(test_intrinsics)
        np.testing.assert_equal(test_intrinsics, gyroscope.GetIntrinsics())
        # Set/get extrinsics.
        test_extrinsics = calico_native.Pose3d()
        test_extrinsics.rotation = [-0.774982, -0.1549964, -0.2324946, 0.5668556]
        test_extrinsics.translation = [1.5, 2.3, 6.8]
        gyroscope.SetExtrinsics(test_extrinsics)
        actual_extrinsics = gyroscope.GetExtrinsics()
        np.testing.assert_allclose(test_extrinsics.rotation,
                                   actual_extrinsics.rotation, 1e-7)
        np.testing.assert_equal(test_extrinsics.translation, actual_extrinsics.translation)
        # Set/get latency.
        test_latency = 0.02
        self.assertTrue(gyroscope.SetLatency(test_latency).ok())
        self.assertEqual(test_latency, gyroscope.GetLatency())
        # Add measurements.
        measurement = calico_native.GyroscopeMeasurement()
        measurement.id.stamp = 0
        measurement.id.sequence = 0
        self.assertTrue(gyroscope.AddMeasurement(measurement).ok())
        measurements = []
        for i in range(3):
            new_measurement = calico_native.GyroscopeMeasurement()
            new_measurement.id.stamp = i + 1
            new_measurement.id.sequence = i + 1
            measurements.append(new_measurement)
        self.assertTrue(gyroscope.AddMeasurements(measurements).ok())

    def test_Camera(self):
        camera = calico_native.Camera()
        # Set/get name.
        test_name = 'test'
        camera.SetName(test_name)
        self.assertEqual(test_name, camera.GetName())
        # Set/get model.
        test_model = (
            calico_native.CameraIntrinsicsModel.kKannalaBrandt)
        self.assertTrue(camera.SetModel(test_model).ok())
        self.assertEqual(test_model, camera.GetModel())
        # Set/get intrinsics.
        test_intrinsics = [1, 2, 3, 4, 5, 6, 7]
        camera.SetIntrinsics(test_intrinsics)
        np.testing.assert_equal(test_intrinsics, camera.GetIntrinsics())
        # Set/get extrinsics.
        test_extrinsics = calico_native.Pose3d()
        test_extrinsics.rotation = [-0.774982, -0.1549964, -0.2324946, 0.5668556]
        test_extrinsics.translation = [1.5, 2.3, 6.8]
        camera.SetExtrinsics(test_extrinsics)
        actual_extrinsics = camera.GetExtrinsics()
        np.testing.assert_allclose(test_extrinsics.rotation,
                                   actual_extrinsics.rotation, 1e-7)
        np.testing.assert_equal(test_extrinsics.translation, actual_extrinsics.translation)
        # Set/get latency.
        test_latency = 0.02
        self.assertTrue(camera.SetLatency(test_latency).ok())
        self.assertEqual(test_latency, camera.GetLatency())
        # Add measurements.
        measurement = calico_native.CameraMeasurement()
        measurement.id.stamp = 0
        measurement.id.image_id = 0
        self.assertTrue(camera.AddMeasurement(measurement).ok())
        measurements = []
        for i in range(3):
            new_measurement = calico_native.CameraMeasurement()
            new_measurement.id.stamp = i + 1
            new_measurement.id.image_id = i + 1
            measurements.append(new_measurement)
        self.assertTrue(camera.AddMeasurements(measurements).ok())

    def test_Trajectory(self):
        trajectory = calico_native.Trajectory()
        poses = {0.0:calico_native.Pose3d(), 1.0:calico_native.Pose3d()}
        trajectory.FitSpline(poses)
        
    def test_Rigidbody(self):
        rigidbody_model_definition = {
            0: [0, 0, 0],
            1: [1, 1, 1],
            2: [2, 2, 2]
        }
        rigidbody_id = 1
        rigidbody_world_pose_is_constant = True
        rigidbody_model_definition_is_constant = True

        rigidbody = calico_native.RigidBody()
        rigidbody.model_definition = dict(rigidbody_model_definition)
        rigidbody.id = rigidbody_id
        rigidbody.world_pose_is_constant = rigidbody_world_pose_is_constant
        rigidbody.model_definition_is_constant = \
            rigidbody_model_definition_is_constant

        for model_id, point in rigidbody.model_definition.items():
            np.testing.assert_equal(rigidbody_model_definition[model_id],
                                    rigidbody.model_definition[model_id])
        self.assertTrue(rigidbody_id, rigidbody.id)
        self.assertTrue(rigidbody_world_pose_is_constant,
                        rigidbody.world_pose_is_constant)
        self.assertTrue(rigidbody_model_definition_is_constant,
                        rigidbody.model_definition_is_constant)

    def test_WorldModel(self):
        world_model = calico_native.WorldModel()

        rigidbody = calico_native.RigidBody()
        rigidbody.model_definition = {
            0: [0, 0, 0],
            1: [1, 1, 1],
            2: [2, 2, 2]
        }
        rigidbody.id = 1
        rigidbody.world_pose_is_constant = True
        rigidbody.model_definition_is_constant = True
        world_model.AddRigidBody(rigidbody)

    def test_BatchOptimizer(self):
        # Stub accelerometer.
        accelerometer = calico_native.Accelerometer()
        self.assertTrue(
            accelerometer.SetModel(
                calico_native.AccelerometerIntrinsicsModel.kAccelerometerScaleOnly
            ).ok())
        accelerometer.SetIntrinsics([1])
        # Stub gyroscope.
        gyroscope = calico_native.Gyroscope()
        self.assertTrue(
            gyroscope.SetModel(
                calico_native.GyroscopeIntrinsicsModel.kGyroscopeScaleOnly
            ).ok())
        gyroscope.SetIntrinsics([1])
        # Stub camera.
        camera = calico_native.Camera()
        self.assertTrue(
            camera.SetModel(calico_native.CameraIntrinsicsModel.kOpenCv5).ok())
        test_camera_intrinsics = [1, 2, 3, 4, 5, 6, 7, 8]
        camera.SetIntrinsics(test_camera_intrinsics)
        # Stub trajectory.
        trajectory = calico_native.Trajectory()
        trajectory.FitSpline({0.0:calico_native.Pose3d(), 1.0:calico_native.Pose3d()})
        # Stub world model.
        world_model = calico_native.WorldModel()
        # Create optimizer.
        optimizer = calico_native.BatchOptimizer()
        optimizer.AddSensor(accelerometer)
        optimizer.AddSensor(gyroscope)
        optimizer.AddSensor(camera)
        optimizer.AddTrajectory(trajectory)
        optimizer.AddWorldModel(world_model)
        summary = optimizer.Optimize()


    def test_camera_model_instantiation(self):
        camera_models = [
            (calico_native.CameraIntrinsicsModel.kOpenCv5, 8),
            (calico_native.CameraIntrinsicsModel.kOpenCv8, 11),
            (calico_native.CameraIntrinsicsModel.kKannalaBrandt, 7),
            (calico_native.CameraIntrinsicsModel.kDoubleSphere, 5),
            (calico_native.CameraIntrinsicsModel.kFieldOfView, 4),
            (calico_native.CameraIntrinsicsModel.kUnifiedCamera, 4),
            (calico_native.CameraIntrinsicsModel.kExtendedUnifiedCamera, 5),
        ]
        for model_type, num_parameters in camera_models:
            camera = calico_native.Camera()
            camera.SetModel(model_type)
            camera.SetIntrinsics(np.random.rand(num_parameters))

    def test_accelerometer_model_instantiation(self):
        accelerometer_models = [
            (calico_native.AccelerometerIntrinsicsModel.kAccelerometerScaleOnly, 1),
            (calico_native.AccelerometerIntrinsicsModel.kAccelerometerScaleAndBias, 4),
            (calico_native.AccelerometerIntrinsicsModel.kAccelerometerVectorNav, 12),
        ]
        for model_type, num_parameters in accelerometer_models:
            accelerometer = calico_native.Accelerometer()
            accelerometer.SetModel(model_type)
            accelerometer.SetIntrinsics(np.random.rand(num_parameters))

    def test_gyroscope_model_instantiation(self):
        gyroscope_models = [
            (calico_native.GyroscopeIntrinsicsModel.kGyroscopeScaleOnly, 1),
            (calico_native.GyroscopeIntrinsicsModel.kGyroscopeScaleAndBias, 4),
            (calico_native.GyroscopeIntrinsicsModel.kGyroscopeVectorNav, 12),
        ]
        for model_type, num_parameters in gyroscope_models:
            gyroscope = calico_native.Gyroscope()
            gyroscope.SetModel(model_type)
            gyroscope.SetIntrinsics(np.random.rand(num_parameters))


if __name__ == '__main__':
    unittest.main()
