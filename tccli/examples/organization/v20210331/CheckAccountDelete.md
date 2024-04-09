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
        "AllowDelete": true,
        "NotAllowReason": {
            "IsCreateMember": true,
            "DeletionPermission": true,
            "IsAssignManager": false,
            "IsAuthManager": false,
            "IsShareManager": false,
            "OperateProcess": false,
            "BillingPermission": true,
            "ExistResources": [],
            "DetectFailedResources": []
        },
        "RequestId": "71295d81-d334-4fc0-af6a-5ac3d5e84b26"
    }
}
```

