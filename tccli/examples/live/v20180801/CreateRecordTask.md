**Example 1: 示例**



Input: 

```
tccli live CreateRecordTask --cli-unfold-argument  \
    --AppName live \
    --DomainName 5000.live.push.com \
    --StreamName livetest \
    --StartTime 1589889600 \
    --EndTime 1589904000 \
    --TemplateId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "UpTbk5RSVhRQFkAAfHwQCCjcRD0lRFcZ0xTSlNTQltlRVRLU1JAWW9EUb"
    }
}
```

