**Example 1: 更新策略**

更新策略

Input: 

```
tccli tag UpdatePolicy --cli-unfold-argument  \
    --Name 地域标签 \
    --Description 地域标签 \
    --Content {"tags":{"Region":{"tag_value":{"@@assign":["ap-guangzhou","ap-beijing"]},"tag_key":{"@@assign":"Region"}}}} \
    --DryRun True \
    --PolicyId 10001
```

Output: 
```
{
    "Response": {
        "RequestId": "74736f60-084c-46ca-8366-93aa7xxxxxx"
    }
}
```

