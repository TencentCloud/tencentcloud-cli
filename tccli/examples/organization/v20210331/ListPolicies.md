**Example 1: 查看策略列表数据**

查看策略列表数据

Input: 

```
tccli organization ListPolicies --cli-unfold-argument  \
    --Scope Local
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AddTime": "2022-08-04 16:04:17",
                "AttachedTimes": 0,
                "Description": "test",
                "PolicyId": 133766838,
                "PolicyName": "test-1",
                "Type": 1,
                "UpdateTime": "2022-08-04 16:04:17"
            },
            {
                "AddTime": "2022-08-04 15:06:07",
                "AttachedTimes": 0,
                "Description": "test-c",
                "PolicyId": 133760482,
                "PolicyName": "test-3",
                "Type": 1,
                "UpdateTime": "2022-08-04 16:03:53"
            }
        ],
        "RequestId": "152482ca-5968-4557-ac1d-1e7ac28ce0da",
        "TotalNum": 2
    }
}
```

