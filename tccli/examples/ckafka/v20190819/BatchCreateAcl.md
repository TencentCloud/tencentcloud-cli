**Example 1: 批量创建ACL**



Input: 

```
tccli ckafka BatchCreateAcl --cli-unfold-argument  \
    --InstanceId xx \
    --ResourceType 2 \
    --RuleList.0.Operation xx \
    --RuleList.0.PermissionType xx \
    --RuleList.0.Host xx \
    --RuleList.0.Principal xx \
    --ResourceNames ******
```

Output: 
```
{
    "Response": {
        "Result": 0,
        "RequestId": "20e995ed-75b9-43bb-84c0-35676567e1a8"
    }
}
```

