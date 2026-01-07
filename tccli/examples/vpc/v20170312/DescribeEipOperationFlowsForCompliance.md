**Example 1: 查询IP历史记录**



Input: 

```
tccli vpc DescribeEipOperationFlowsForCompliance --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EipOperationFlowSet": [
            {
                "IpAddress": "1.12.234.33",
                "Uin": "100034335304",
                "BeginTime": "2024-09-24 00:00:00",
                "EndTime": "2024-12-01 09:08:27",
                "InstanceIds": [
                    "lhins-d1savla9"
                ],
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "f5d78a62-f2f3-4929-8a32-8b8477e1148d"
    }
}
```

