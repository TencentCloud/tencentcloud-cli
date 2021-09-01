**Example 1: 设置云数据库实例账户密码**



Input: 

```
tccli mongodb SetPassword --cli-unfold-argument  \
    --InstanceId cmgo-eqmoa5sf \
    --UserName test_user \
    --Password test_password123
```

Output: 
```
{
    "Response": {
        "FlowId": 1082,
        "RequestId": "a02372cf-5e09-4d17-ab79-2ee3f60e86ff"
    }
}
```

