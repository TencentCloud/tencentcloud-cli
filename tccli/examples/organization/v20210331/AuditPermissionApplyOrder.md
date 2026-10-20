**Example 1: 审批申请**



Input: 

```
tccli organization AuditPermissionApplyOrder --cli-unfold-argument  \
    --ZoneId z-a1b2c3d4e5 \
    --ApplyId apply-3f5a7c9e1b2d4f6a \
    --AuditResult Reject \
    --AuditOpinion 权限范围过大，请拆分后重新申请
```

Output: 
```
{
    "Response": {
        "Tasks": [],
        "RequestId": "43eb5472-38f1-403f-b3a0-592cc5785a05"
    }
}
```

