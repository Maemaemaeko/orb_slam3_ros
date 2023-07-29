import rosbag
import pandas as pd

# Step 1: Specify the ROS bag file path
rosbag_file = "/home/myamaguchi/catkin_ws/demo_data/vicon_system/rgbd_2023-07-28-12-37-18_2023-07-29-20-55-06.bag"
# Step 2: Extract data from the ROS bag
timestamps = []
positions_x = []
positions_y = []
positions_z = []
quaternions_w = []
quaternions_x = []
quaternions_y = []
quaternions_z = []

with rosbag.Bag(rosbag_file, "r") as bag:
    for topic, msg, t in bag.read_messages():
        if topic == "/orb_slam3/camera_pose":  # Replace "your_topic_name" with the actual topic name.
            timestamps.append(msg.header.stamp.secs*10**9 + msg.header.stamp.nsecs)
            positions_x.append(msg.pose.position.x)
            positions_y.append(msg.pose.position.y)
            positions_z.append(msg.pose.position.z)
            quaternions_w.append(msg.pose.orientation.w)
            quaternions_x.append(msg.pose.orientation.x)
            quaternions_y.append(msg.pose.orientation.y)
            quaternions_z.append(msg.pose.orientation.z)

# Step 3: Create a DataFrame and save it in the desired format
data = {
    "#timestamp [ns]": timestamps,
    "p_RS_R_x [m]": positions_x,
    "p_RS_R_y [m]": positions_y,
    "p_RS_R_z [m]": positions_z,
    "q_RS_w []": quaternions_w,
    "q_RS_x []": quaternions_x,
    "q_RS_y []": quaternions_y,
    "q_RS_z []": quaternions_z,
}

df = pd.DataFrame(data)
df.to_csv("/home/myamaguchi/catkin_ws/src/orb_slam3_ros/evaluation/Results/vicon_system/rgbd_2023-07-28-12-37-18_2023-07-29-20-55-06.txt", index=False, float_format="%.10f")
