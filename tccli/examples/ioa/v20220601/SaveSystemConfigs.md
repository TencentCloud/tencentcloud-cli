**Example 1: 示例1**



Input: 

```
tccli ioa SaveSystemConfigs --cli-unfold-argument  \
    --OsType xx \
    --Configs.0.Description xx \
    --Configs.0.Modify 0 \
    --Configs.0.Value xx \
    --Configs.0.Version 0 \
    --Configs.0.OsType xx \
    --Configs.0.Id 0 \
    --Configs.0.Name xx \
    --DomainIds 0 \
    --DomainId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

