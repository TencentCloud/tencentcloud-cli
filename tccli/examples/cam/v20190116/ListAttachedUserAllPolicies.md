**Example 1: 列出用户关联的策略（包括随组关联）**



Input: 

```
tccli cam ListAttachedUserAllPolicies --cli-unfold-argument  \
    --Rp 1 \
    --Page 10 \
    --AttachType 1 \
    --TargetUin 100020328651
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "PolicyList": [
            {
                "AddTime": "2020-01-16 15:09:27",
                "CreateMode": "2",
                "Deactived": 1,
                "DeactivedDetail": [
                    "consolesms"
                ],
                "Description": "短信（SMS）全读写访问权限",
                "Groups": [
                    {
                        "GroupId": 93878,
                        "GroupName": "系统运维"
                    }
                ],
                "PolicyId": "219064",
                "PolicyName": "QcloudSMSFullAccess",
                "StrategyType": "2"
            }
        ],
        "RequestId": "d369dabb-ebc9-4598-baae-e1177e9e3868"
    }
}
```

