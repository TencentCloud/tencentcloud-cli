**Example 1: 创建标签策略**

创建标签策略

Input: 

```
tccli tag CreatePolicy --cli-unfold-argument  \
    --Content {"tags":{"Region":{"tag_value":{"@@assign":["ap-guangzhou","ap-beijing"]},"tag_key":{"@@assign":"Region"}}}} \
    --DryRun false \
    --Name 地域标签 \
    --Description 地域标签
```

Output: 
```
{
    "Response": {
        "PolicyId": 10001,
        "RequestId": "74736f60-084c-46ca-8366-93aa7830f9c8"
    }
}
```

