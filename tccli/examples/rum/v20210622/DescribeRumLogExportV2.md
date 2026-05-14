**Example 1: success**



Input: 

```
tccli rum DescribeRumLogExportV2 --cli-unfold-argument  \
    --Name 20250520160524 \
    --StartTime 1665993060000 \
    --Filter [{"Key": "instanceId", "Operator": "eq", "Value": "rum-xyz"}] \
    --EndTime 1665996660000 \
    --ID 100 \
    --Fields msg url
```

Output: 
```
{
    "Response": {
        "RequestId": "81a43a52-d00f-462a-82da-89841117f4ca",
        "Result": "{\"code\": 0, \"data\": {\"id\": 1, \"name\": \"132445_log\", \"message\": \"export log\"}, \"msg\": \"export log success\"}"
    }
}
```

