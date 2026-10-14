**Example 1: 成功示例**



Input: 

```
tccli iss DescribeVLPlanResult --cli-unfold-argument  \
    --VLPlanResultId 4537*****************************30b
```

Output: 
```
{
    "Response": {
        "Data": {
            "BilledFrameCount": 60,
            "ChannelId": "319c*****************************d4e",
            "ChannelName": "海康PTZ球机**",
            "Content": "{\"has_fall\":false,\"fall_events\":[],\"summary\":\"视频中未检测到老人跌倒事件。画面全程为静止的办公椅特写，无人员出现或任何动作发生。\"}",
            "CreatedAt": "2026-10-10 18:51:54",
            "DeviceId": "4662*****************************c8c",
            "DeviceName": "HikNVR*********",
            "ImageUrl": "",
            "ImageUrlExpire": 300,
            "MediaType": "video",
            "OrganizationId": "236",
            "OrganizationName": "西安市",
            "SnapshotTimestamp": 0,
            "UpdatedAt": "2026-10-10 18:51:54",
            "VLPlanId": "VPe2***************************eec",
            "VLPlanName": "",
            "VLPlanResultId": "4537*****************************30b",
            "VLResultTimestamp": 1791629513,
            "VideoEndTimestamp": 1791629460,
            "VideoStartTimestamp": 1791629400
        },
        "RequestId": "6e538216-22fe-4e4b-b0be-c03647185ee4"
    }
}
```

