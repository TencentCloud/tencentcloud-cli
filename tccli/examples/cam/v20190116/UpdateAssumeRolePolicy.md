**Example 1: 修改角色信任策略**



Input: 

```
tccli cam UpdateAssumeRolePolicy --cli-unfold-argument  \
    --RoleId 4611686018427731422 \
    --PolicyDocument %7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22action%22%3A%22name%2Fsts%3AAssumeRole%22%2C%22effect%22%3A%22allow%22%2C%22principal%22%3A%7B%22service%22%3A%5B%22cloudaudit.cloud.tencent.com%22%2C%22cls.cloud.tencent.com%22%5D%7D%7D%5D%7D
```

Output: 
```
{
    "Response": {
        "RequestId": "69103fca-ec49-40c9-8986-788b57421501"
    }
}
```

