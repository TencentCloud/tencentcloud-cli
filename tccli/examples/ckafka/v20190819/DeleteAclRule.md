**Example 1: 删除ACL规则示例**



Input: 

```
tccli ckafka DeleteAclRule --cli-unfold-argument  \
    --InstanceId ckafka-123456 \
    --RuleName testRule
```

Output: 
```
{
    "Response": {
        "Result": 12,
        "RequestId": "8c3daa3a-d87b-47ef-9ddd-f0905eeb8d84"
    }
}
```

