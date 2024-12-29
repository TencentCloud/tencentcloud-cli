**Example 1: 查询所有的直播流监播任务**

返回所有监播场次列表，包含各监播场次的基本信息

Input: 

```
tccli live DescribeLiveStreamMonitorList --cli-unfold-argument  \
    --Index 0 \
    --Count 1
```

Output: 
```
{
    "Response": {
        "LiveStreamMonitors": [
            {
                "MonitorId": "1bd5af00-5be5-4e4d-aa75-340ba0f35586",
                "MonitorName": "",
                "OutputInfo": {
                    "OutputStreamName": "example_output_stream_name",
                    "OutputStreamWidth": 1920,
                    "OutputStreamHeight": 1080,
                    "OutputDomain": "",
                    "OutputApp": ""
                },
                "Status": 1,
                "StartTime": 1640694582,
                "StopTime": 1640591812,
                "InputList": [
                    {
                        "InputStreamName": "example_stream_name",
                        "Description": "",
                        "InputDomain": "",
                        "InputApp": "",
                        "InputUrl": ""
                    }
                ],
                "CheckStreamBroken": 1,
                "AsrLanguage": 1,
                "UpdateTime": 1640694582,
                "OcrLanguage": 1,
                "NotifyPolicy": {
                    "CallbackUrl": "www.baidu.com",
                    "NotifyPolicyType": 0
                },
                "CreateTime": 1640694582,
                "AiAsrInputIndexList": [
                    1
                ],
                "AiFormatDiagnose": 1,
                "AiOcrInputIndexList": [
                    1
                ],
                "CheckStreamLowFrameRate": 1,
                "AudibleInputIndexList": [
                    1
                ],
                "AllowMonitorReport": 1,
                "AiQualityControl": 1
            }
        ],
        "TotalNum": 7,
        "RequestId": "3f3fd3ae-23a1-44dc-94d6-35380052b4f4"
    }
}
```

