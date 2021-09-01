**Example 1: 示例**



Input: 

```
tccli live DescribeRecordTask --cli-unfold-argument  \
    --AppName live \
    --DomainName 5000.live.push.com \
    --StreamName livetest \
    --StartTime 1595779200 \
    --EndTime 1595865600
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "ScrollToken": "",
        "TaskList": [
            {
                "TaskId": "UpTbk5RSVhRQFkAAfHwQCCjcRD0lRFcZ0xTSlNTQltlRVRLU1JAWW9EUb",
                "DomainName": "5000.live.push.com",
                "AppName": "live",
                "StreamName": "livetest",
                "StartTime": 1595779900,
                "EndTime": 1595789900,
                "TemplateId": 123,
                "Stopped": 1595783500
            },
            {
                "TaskId": "UpTbk5RSVhRQFkAAfHwQCCjcRD0lRFcZ0xTSlNTQltlRVRLFszdDWW9EUb",
                "DomainName": "5000.live.push.com",
                "AppName": "live",
                "StreamName": "livetest",
                "StartTime": 1595789900,
                "EndTime": 1595799900,
                "TemplateId": 0,
                "Stopped": 0
            }
        ]
    }
}
```

