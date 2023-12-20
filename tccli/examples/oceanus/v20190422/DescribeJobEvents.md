**Example 1: 查询作业事件**



Input: 

```
tccli oceanus DescribeJobEvents --cli-unfold-argument  \
    --RunningOrderIds 1 \
    --Types 1 2 \
    --EndTimestamp 1630933910 \
    --StartTimestamp 1630833910 \
    --JobId cql-21f5a2ve
```

Output: 
```
{
    "Response": {
        "RunningOrderIds": [
            1
        ],
        "Events": [
            {
                "RunningOrderId": 1,
                "Description": "作业停止事件",
                "Timestamp": 1630933810,
                "Type": "11"
            }
        ],
        "TotalCount": 1,
        "RequestId": "123345be-e89b-52f3-a456-426616274040"
    }
}
```

