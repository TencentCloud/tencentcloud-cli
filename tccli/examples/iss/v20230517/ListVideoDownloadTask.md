**Example 1: 成功**

   

Input: 

```
tccli iss ListVideoDownloadTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelCode": "310****00001320000001",
                    "ChannelId": "21098feb-57a4-4fbc-9435-************",
                    "ChannelName": "11",
                    "DeviceCode": "610*****01180000159",
                    "DeviceName": "NVR",
                    "DownloadTaskId": "e6651293-b5fa-4dbb-bfe0-************",
                    "DownloadTime": 7200,
                    "EndTime": "2024-10-22 12:29:02",
                    "Expire": 7,
                    "FailedReason": "",
                    "FileDownloadUrl": "https://*********.demo.cn/vds/lr/video.mp4?source=localrecord%2F7%2F21098feb-57a4-4fbc-9435-************%2F20241021%2Fe6651293-b5fa-4dbb-bfe0-************.mp4%3Bivc-test-new-251228313-ap-shanghai-1258344699%3Bap-shanghai%3B21098feb-57a4-4fbc-9435-*********%3B251228313%3B7000003*****9&intranet=0&expires=3600&signtime=1729675136&sign=1f9f2d21eb5e18b088f70f81*********",
                    "Scale": 2,
                    "StartTime": "2024-10-22 11:28:36",
                    "Status": 2,
                    "VideoSize": 967309246,
                    "VideoTimeSection": "2024-10-21 08:00:00-2024-10-21 10:00:00"
                }
            ],
            "TotalCount": 15
        },
        "RequestId": "f5447c9b-a7a6-42d5-b831-9e666bfbe261"
    }
}
```

