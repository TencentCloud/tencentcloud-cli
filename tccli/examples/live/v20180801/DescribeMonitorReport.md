**Example 1: 查询某个监播报告**

调用该接口，返回7天内所有报告信息

Input: 

```
tccli live DescribeMonitorReport --cli-unfold-argument  \
    --MonitorId 1bd5af00-5be5-4e4d-aa75-340ba0f35586
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "MPSResult": {
            "AiAsrResults": [],
            "AiOcrResults": []
        },
        "DiagnoseResult": {
            "StreamBrokenResults": []
        }
    }
}
```

