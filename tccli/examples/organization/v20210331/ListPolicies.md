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
                "Description": "deny policy",
                "PolicyId": 10001,
                "PolicyName": "policy_name",
                "Type": 1,
                "UpdateTime": "2022-08-04 16:04:17"
            }
        ],
        "RequestId": "152482ca-5968-4557-ac1d-1e7ac28ce0da",
        "TotalNum": 1
    }
}
```

