**Example 1: 查询容灾策略操作掩码**

传入一批容灾策略ID，返回每个策略当前不允许执行的操作列表（包含操作名、错误码与错误信息）。

Input: 

```
tccli bdrc DescribeDisasterRecoverySitePairsDeniedActions --cli-unfold-argument  \
    --SitePairIds sitepair-2zjmpdlb
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d",
        "SitePairDeniedActionSet": [
            {
                "DeniedActions": [
                    {
                        "Action": "DeleteDisasterRecoverySitePair",
                        "Code": "SitePairOperationConflict",
                        "Message": "当前容灾策略存在未完成的任务，禁止执行该操作"
                    }
                ],
                "SitePairId": "sitepair-2zjmpdlb"
            }
        ]
    }
}
```

