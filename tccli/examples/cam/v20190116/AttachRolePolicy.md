**Example 1: 绑定权限策略到角色**

以下示例将绑定一个策略到指定的角色

Input: 

```
tccli cam AttachRolePolicy --cli-unfold-argument  \
    --PolicyId 1 \
    --AttachRoleId 4611686018427397905
```

Output: 
```
{
    "Response": {
        "RequestId": "0b55ef5b-36b1-4649-8bb9-1aca465f17fb"
    }
}
```

