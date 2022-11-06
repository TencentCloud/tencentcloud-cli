**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlowLogs --cli-unfold-argument  \
    --FlowId 0175723949ba0956b92d0bf40cfe \
    --StartTime 2020-12-10T13:00:00Z \
    --EndTime 2020-12-10T13:27:00Z \
    --Type Input Output \
    --Pipeline 0 1 \
    --PageNum 1 \
    --PageSize 100
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Timestamp": 1607605513,
                "Type": "input",
                "InputOutputId": "0175723949bb0956b92d0bf40cff",
                "Protocol": "srt",
                "EventCode": "1000",
                "EventMessage": "Access Granted",
                "RemoteIp": "42.194.229.84",
                "RemotePort": "29000",
                "Pipeline": "xx",
                "InputOutputName": "xx"
            }
        ],
        "PageNum": 1,
        "PageSize": 100,
        "RequestId": "137253816",
        "TotalNum": 3,
        "TotalPage": 1
    }
}
```

