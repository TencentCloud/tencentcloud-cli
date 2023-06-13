**Example 1: 查询策略**

查询策略

Input: 

```
tccli camp DescribePolicy --cli-unfold-argument  \
    --ProjectID abc \
    --ApplicationID abc \
    --InstanceID abc \
    --EnvironmentName abc \
    --PolicyName abc
```

Output: 
```
{
    "Response": {
        "Policy": {},
        "RequestId": "abc"
    }
}
```

