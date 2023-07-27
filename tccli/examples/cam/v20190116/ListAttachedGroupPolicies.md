**Example 1: 查询用户组关联的策略列表**

查询用户组3349关联的策略列表

Input: 

```
tccli cam ListAttachedGroupPolicies --cli-unfold-argument  \
    --TargetGroupId 3349 \
    --Page 1 \
    --Rp 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "OperateOwnerUin": "10001",
                "PolicyName": "AdministratorAccess",
                "Remark": "test policy remark",
                "OperateUinType": 1,
                "CreateMode": 1,
                "Deactived": 1,
                "AddTime": "2020-09-22 00:00:00",
                "PolicyType": "User",
                "PolicyId": 1,
                "DeactivedDetail": [
                    "test"
                ],
                "OperateUin": "10001"
            }
        ],
        "RequestId": "836d7034-9854-44f0-9d4a-ee57842f8644",
        "TotalNum": 1
    }
}
```

