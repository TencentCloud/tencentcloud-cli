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
                "PolicyName": "test-0103",
                "AddTime": "2022-01-03 10:38:28",
                "CreateMode": 3,
                "Remark": "",
                "OperateOwnerUin": null,
                "OperateUin": null,
                "OperateUinType": null,
                "PolicyType": "",
                "Deactived": 0,
                "DeactivedDetail": []
            }
        ],
        "TotalNum": 1,
        "RequestId": "db1cdf3f-9b1a-47c5-88b3-c49089aaa811"
    }
}
```

