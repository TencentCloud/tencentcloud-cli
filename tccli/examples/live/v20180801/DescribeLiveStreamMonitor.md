**Example 1: 查询某个监播任务配置**

查询某个监播场次，返回该场次的基本配置信息。

Input: 

```
tccli live DescribeLiveStreamMonitor --cli-unfold-argument  \
    --MonitorId 1bd5af00-5be5-4e4d-aa75-340ba0f35586
```

Output: 
```
{
    "Response": {
        "LiveStreamMonitor": {
            "MonitorId": "1bd5af00-5be5-4e4d-aa75-340ba0f35586",
            "MonitorName": "example_monitor_name",
            "OutputInfo": {
                "OutputStreamName": "example_output_stream_name",
                "OutputStreamWidth": 1920,
                "OutputStreamHeight": 1080,
                "OutputDomain": "",
                "OutputApp": ""
            },
            "InputList": [
                {
                    "InputStreamName": "example_stream_name",
                    "InputDomain": "",
                    "InputApp": "",
                    "InputUrl": "",
                    "Description": ""
                }
            ],
            "Status": 1,
            "CreateTime": 1640694582,
            "UpdateTime": 1640591812,
            "NotifyPolicy": {
                "NotifyPolicyType": 1,
                "CallbackUrl": "xx"
            },
            "AudibleInputIndexList": [
                1
            ],
            "AiAsrInputIndexList": [
                1
            ],
            "CheckStreamBroken": 1,
            "CheckStreamLowFrameRate": 1,
            "AsrLanguage": 1,
            "OcrLanguage": 1
        },
        "RequestId": ""
    }
}
```

