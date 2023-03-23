**Example 1: 添加 ACL 规则示例**



Input: 

```
tccli ckafka CreateAclRule --cli-unfold-argument  \
    --InstanceId ckafka-12345678 \
    --ResourceType Topic \
    --RuleList.0.Host 1.2.3.4 \
    --RuleList.0.Principal User:* \
    --RuleList.0.Operation WRITE \
    --RuleList.0.PermissionType ALLOW \
    --RuleName testRule \
    --PatternType PREFIXED \
    --Pattern testPattern
```

Output: 
```
{
    "Response": {
        "Result": 12,
        "RequestId": "8c3daa3a-d87b-47ef-9ccd-f0905eeb8d84"
    }
}
```

