**Example 1: 删除治理中心命名空间**



Input: 

```
tccli tse DeleteGovernanceNamespaces --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceNamespaces.0.Name abc
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

