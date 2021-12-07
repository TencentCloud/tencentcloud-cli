**Example 1: 查询workload类型的影响范围示例**



Input: 

```
tccli tcss DescribeAffectedWorkloadList --cli-unfold-argument  \
    --CheckItemId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ea73ee35-ec93-4d94-b2fc-979a58f34be1",
        "TotalCount": 0,
        "AffectedWorkloadList": []
    }
}
```

