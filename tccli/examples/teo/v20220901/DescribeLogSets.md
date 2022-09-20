**Example 1: 获取日志集列表**



Input: 

```
tccli teo DescribeLogSets --cli-unfold-argument  \
    --LogSetRegion ap-guanghzou
```

Output: 
```
{
    "Response": {
        "LogSetList": [
            {
                "Deleted": "no",
                "LogSetId": "ae803624-ee6a-4a14-a716-1dee1a8f6f7b",
                "LogSetName": "test_log",
                "LogSetRegion": "ap-guangzhou"
            }
        ],
        "TotalCount": 1,
        "RequestId": "a3fdb9f1-c97e-4d7e-86ac-aa15f27b2239"
    }
}
```

