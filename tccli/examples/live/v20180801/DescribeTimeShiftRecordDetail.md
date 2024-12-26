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
        "RequestId": "27b51725-321e-4347-8906-4e1d94b5a373",
        "RecordList": [
            {
                "Sid": "2980018187870252785",
                "StartTime": 1668064484,
                "EndTime": 1668064584
            }
        ]
    }
}
```

