**Example 1: 请求示例**



Input: 

```
tccli live DescribePullTransformPushInfoList --cli-unfold-argument  \
    --EndTime 2022-08-17T16:15:00+08:00 \
    --StartTime 2022-08-17T16:05:00+08:00 \
    --TaskId 123468
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "VideoFps": 61,
                "AudioFps": 48,
                "VideoRate": 3564625,
                "AudioRate": 137809,
                "StreamFlag": "3567",
                "Time": "2022-08-17T16:05:00+08:00"
            }
        ],
        "RequestId": "853d1eb7-8299-482b-b99b-f04f59c6a23d"
    }
}
```

