**Example 1: 删除治理中心服务**



Input: 

```
tccli tse DeleteGovernanceServices --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceServices.0.Name abc \
    --GovernanceServices.0.Namespace abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

