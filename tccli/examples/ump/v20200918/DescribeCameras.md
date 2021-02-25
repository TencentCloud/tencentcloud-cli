**Example 1: 获取摄像头状态列表**



Input: 

```
tccli ump DescribeCameras --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Cameras": [
            {
                "CameraFeature": 1,
                "CameraId": 1,
                "CameraName": "camera_name",
                "Pixel": "100w",
                "CameraIp": "ip",
                "CameraState": 0,
                "RTSP": "rtsp://192.168.1.1/av0_0",
                "Zones": [
                    {
                        "ZoneId": 1,
                        "ZoneName": "zone_name",
                        "BunkCodes": "bunk_codes"
                    }
                ]
            }
        ]
    }
}
```

