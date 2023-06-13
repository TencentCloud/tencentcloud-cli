**Example 1: 查询策略列表**

查询策略列表

Input: 

```
tccli camp DescribePolicies --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Query abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Policies": [
            {}
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

