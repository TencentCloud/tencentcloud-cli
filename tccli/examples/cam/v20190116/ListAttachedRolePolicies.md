**Example 1: 获取角色绑定的策略列表**



Input: 

```
tccli cam ListAttachedRolePolicies --cli-unfold-argument  \
    --RoleId 4611686018427397905\
    --Page 1\
    --Rp 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyId": 13847366,
                "PolicyName": "QcloudAccessForASRole",
                "AddTime": "2019-07-10 11:17:41",
                "CreateMode": 2,
                "PolicyType": "QCS"
            }
        ],
        "TotalNum": 1,
        "RequestId": "60dc7f3f-5d8b-45e9-b703-5feefac9960c"
    }
}
```

