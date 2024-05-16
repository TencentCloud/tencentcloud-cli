**Example 1: 创建一个角色**

以下示例将创建一个以日志服务和操作审计为载体的角色

Input: 

```
tccli cam CreateRole --cli-unfold-argument  \
    --RoleName test_1234544 \
    --PolicyDocument %7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22action%22%3A%22name%2Fsts%3AAssumeRole%22%2C%22effect%22%3A%22allow%22%2C%22principal%22%3A%7B%22service%22%3A%5B%22cloudaudit.cloud.tencent.com%22%2C%22cls.cloud.tencent.com%22%5D%7D%7D%5D%7D \
    --Description abc
```

Output: 
```
{
    "Response": {
        "RoleId": "123456789000",
        "RequestId": "0bac591a-6cc7-4e9d-8d01-74618f1a9611"
    }
}
```

