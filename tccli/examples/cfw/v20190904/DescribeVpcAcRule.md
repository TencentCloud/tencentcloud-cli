**Example 1: 查询内网间访问控制列表**

查询内网间访问控制列表

Input: 

```
tccli cfw DescribeVpcAcRule --cli-unfold-argument  \
    --Filters.0.Name Protocol \
    --Filters.0.Values ANY TCP ICMP \
    --Filters.0.OperatorType 9 \
    --Limit 10 \
    --Offset 0 \
    --Order desc \
    --By sequence
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "SourceContent": "abc",
                "SourceType": "abc",
                "DestContent": "abc",
                "DestType": "abc",
                "Protocol": "abc",
                "RuleAction": "abc",
                "Port": "abc",
                "Description": "abc",
                "OrderIndex": 0,
                "Uuid": 0,
                "Enable": "abc",
                "EdgeId": "abc",
                "DetectedTimes": 0,
                "EdgeName": "abc",
                "InternalUuid": 0,
                "Deleted": 0,
                "FwGroupId": "abc",
                "FwGroupName": "abc",
                "BetaList": [
                    {
                        "TaskId": 0,
                        "TaskName": "abc",
                        "LastTime": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

