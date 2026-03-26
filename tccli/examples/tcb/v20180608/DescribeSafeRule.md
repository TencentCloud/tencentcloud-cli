**Example 1: 获取环境下某个集合安全规则**

获取环境下某个集合安全规则

Input: 

```
tccli tcb DescribeSafeRule --cli-unfold-argument  \
    --EnvId my-env-cxuiytejgkldjk \
    --CollectionName my-table
```

Output: 
```
{
    "Response": {
        "AclTag": "READONLY",
        "Rule": "",
        "RequestId": "2bced453-09e4-4e87-9317-c3bc21c4ee22"
    }
}
```

