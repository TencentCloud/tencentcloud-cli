**Example 1: 查询实例hai-xxxxxxxx包含的服务登录配置**

查询实例hai-xxxxxxxx包含的服务登录配置

Input: 

```
tccli hai DescribeServiceLoginSettings --cli-unfold-argument  \
    --InstanceId hai-xxxxxxxx \
    --ServiceName jupyter
```

Output: 
```
{
    "Response": {
        "RequestId": "73956f5a-0f0e-4e60-ba7d-d555bcefe27b",
        "LoginSettings": [
            {
                "ServiceName": "jupyter",
                "Url": "http://1.14.52.185:80?40a0153b6c8ff839b2b83f9a3918daa55facad3c3e7a9b4a0e2377bd08f4aaa2"
            }
        ]
    }
}
```

