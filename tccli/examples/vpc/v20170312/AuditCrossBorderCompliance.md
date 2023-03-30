**Example 1: 合规化审批**

本接口（AuditCrossBorderCompliance）用于服务商操作合规化资质审批。

Input: 

```
tccli vpc AuditCrossBorderCompliance --cli-unfold-argument  \
    --ServiceProvider UNICOM \
    --ComplianceId 10006 \
    --AuditBehavior DENY
```

Output: 
```
{
    "Response": {
        "RequestId": "0de0923a-c53c-43c2-9c25-99b2f3944107"
    }
}
```

