**Example 1: 查询子账号关联的策略列表**

查询绑定到子账号3449203261的策略列表

Input: 

```
tccli cam ListAttachedUserPolicies --cli-unfold-argument  \
    --TargetUin 3449203261 \
    --Page 1 \
    --Rp 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyId": 1,
                "PolicyName": "AdministratorAccess",
                "AddTime": "2018-04-09 16:31:19",
                "CreateMode": 2,
                "PolicyType": "User"
            }
        ],
        "TotalNum": 1,
        "RequestId": "836d7034-9854-44f0-9d4a-ee57842f8644"
    }
}
```

