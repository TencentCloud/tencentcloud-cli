**Example 1: 获取摄像头配置信息**



Input: 

```
tccli ump DescribeConfig --cli-unfold-argument  \
    --ServerMac 78:7B:8A:CD:1D:EA \
    --GroupCode  \
    --MallId 0 \
    --CameraSign sign \
    --CameraAppId  \
    --CameraTimestamp 1599655851520 \
    --SessionId id
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "SessionId": "id",
        "Version": 1,
        "Cameras": [
            {
                "GroupCode": "",
                "MallId": 1,
                "FloorId": 1,
                "CameraId": 1,
                "CameraIp": "ip",
                "CameraMac": "mac",
                "CameraType": 2,
                "CameraFeature": 1,
                "CameraState": 0,
                "Width": 1920,
                "Height": 1080,
                "ZoneId": 1,
                "ZoneType": 1,
                "Config": {
                    "CameraProducer": "D",
                    "RTSP": "",
                    "Fps": 5,
                    "DecodeFps": 5,
                    "PassengerFlow": 1,
                    "FaceExpose": 1,
                    "MallArea": [
                        {
                            "X": 1,
                            "Y": 1
                        },
                        {
                            "X": 2,
                            "Y": 2
                        },
                        {
                            "X": 3,
                            "Y": 3
                        }
                    ],
                    "ShopArea": [
                        {
                            "X": 1,
                            "Y": 1
                        },
                        {
                            "X": 2,
                            "Y": 2
                        },
                        {
                            "X": 3,
                            "Y": 3
                        }
                    ],
                    "TrackAreas": [
                        {
                            "Points": [
                                {
                                    "X": 1,
                                    "Y": 1
                                },
                                {
                                    "X": 2,
                                    "Y": 2
                                },
                                {
                                    "X": 3,
                                    "Y": 3
                                },
                                {
                                    "X": 4,
                                    "Y": 4
                                }
                            ]
                        }
                    ],
                    "Zones": [
                        {
                            "ZoneId": 1,
                            "ShopArea": [
                                {
                                    "X": 1,
                                    "Y": 1
                                },
                                {
                                    "X": 2,
                                    "Y": 2
                                },
                                {
                                    "X": 3,
                                    "Y": 3
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```

