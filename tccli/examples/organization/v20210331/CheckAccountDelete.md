**Example 1: 成员账号删除检查**

成员账号删除检查

Input: 

```
tccli organization CheckAccountDelete --cli-unfold-argument  \
    --MemberUin 111111111111
```

Output: 
```
{
    "Response": {
        "AllowDelete": false,
        "NotAllowReason": {
            "IsCreateMember": true,
            "DeletionPermission": true,
            "IsAssignManager": true,
            "IsAuthManager": true,
            "IsShareManager": true,
            "OperateProcess": true,
            "BillingPermission": true,
            "ExistResources": [],
            "DetectFailedResources": []
        },
        "RequestId": "71295d81-d334-4fc0-af6a-5ac3d5e84b26"
    }
}
```

