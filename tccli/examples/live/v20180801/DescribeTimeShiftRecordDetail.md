**Example 1: DescribeTimeShiftRecordDetail**

查询时移流录制详情

Input: 

```
tccli live DescribeTimeShiftRecordDetail --cli-unfold-argument  \
    --Domain 5000.live.push.com \
    --AppName live \
    --StreamName livetest \
    --StartTime 1668064484 \
    --EndTime 1668064584 \
    --DomainGroup  \
    --TransCodeId 330587
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "RecordList": [
            {
                "Sid": "xxx",
                "StartTime": 1668064484,
                "EndTime": 1668064584
            }
        ]
    }
}
```

