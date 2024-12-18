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
                "PolicyId": 109360057,
                "PolicyName": "policygen-20240909141614",
                "AddTime": "2024-09-09 15:51:40",
                "CreateMode": 3,
                "Remark": "cos policy",
                "OperateOwnerUin": "100008847111",
                "OperateUin": "100008847111",
                "OperateUinType": 0,
                "PolicyType": "User",
                "Deactived": 0,
                "DeactivedDetail": [
                    "ccs"
                ]
            }
        ],
        "TotalNum": 1,
        "RequestId": "db1cdf3f-9b1a-47c5-88b3-c49089aaa811"
    }
}
```

