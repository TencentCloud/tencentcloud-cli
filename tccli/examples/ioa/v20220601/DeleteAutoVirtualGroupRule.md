**Example 1: 示例1**

删除自动划分规则

Input: 

```
tccli ioa DeleteAutoVirtualGroupRule --cli-unfold-argument  \
    --VirtualGroupId 7 \
    --OsType 0 \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Ok": true,
            "RuleId": 1
        },
        "RequestId": "498da19e-8cdb-40e0-a203-4795ac2deeee"
    }
}
```

**Example 2: 删除自定义分组自动划分规则**

删除自定义分组自动划分规则

Input: 

```
tccli ioa DeleteAutoVirtualGroupRule --cli-unfold-argument  \
    --DomainInstanceId 3 \
    --VirtualGroupId 8 \
    --OsType 0 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Ok": true,
            "RuleId": 1
        },
        "RequestId": "d7dd4467-ff51-4e66-9c4a-7df1ce7acde0"
    }
}
```

