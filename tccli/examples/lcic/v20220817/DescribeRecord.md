**Example 1: 查询录制信息**



Input: 

```
tccli lcic DescribeRecord --cli-unfold-argument  \
    --SdkAppId 34234 \
    --RoomId 1242
```

Output: 
```
{
    "Response": {
        "ClassId": 343121517,
        "RecordInfo": [
            {
                "Duration": 274,
                "FileFormat": "mp4",
                "RecordSize": 3172788,
                "RecordUrl": "https://10018181/1fe1c5e51397757897946447816/f0.mp4",
                "StartTime": 1732094036,
                "StopTime": 1732094310,
                "TaskId": "c2f8969d0d-5971-95f5-a07f6efcecb9",
                "VideoId": "1397797946447816"
            }
        ],
        "RequestId": "cba5909ae-8924-4ae6-850e-099332ffd535",
        "SchoolId": 3523371
    }
}
```

