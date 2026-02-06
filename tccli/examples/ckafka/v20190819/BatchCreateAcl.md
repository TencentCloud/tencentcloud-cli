**Example 1: 批量创建ACL**



Input: 

```
tccli ckafka BatchCreateAcl --cli-unfold-argument  \
    --InstanceId ckafka-xx \
    --ResourceType 2 \
    --RuleList.0.Operation Read \
    --RuleList.0.PermissionType Allow \
    --RuleList.0.Host 10.1.1.0/24 \
    --RuleList.0.Principal User:* \
    --ResourceNames rewr topic-1
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

