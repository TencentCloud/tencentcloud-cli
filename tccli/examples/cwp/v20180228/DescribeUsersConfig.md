**Example 1: 查询用户自定义配置**

查询用户自定义配置

Input: 

```
tccli cwp DescribeUsersConfig --cli-unfold-argument  \
    --ConfigName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "fd768174-3c72-4c62-8fa0-fd0106d31494",
        "Value": "1"
    }
}
```

