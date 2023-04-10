**Example 1: 自定义账号**

自定义实例账号

Input: 

```
tccli mongodb CreateAccountUser --cli-unfold-argument  \
    --InstanceId cmgo-9d0p**** \
    --UserName test_user \
    --Password Abc@123... \
    --MongoUserPassword Abc@123... \
    --UserDesc 测试用户 \
    --AuthRole.0.Mask 0 \
    --AuthRole.0.NameSpace collection
```

Output: 
```
{
    "Response": {
        "FlowId": 1680767468,
        "RequestId": "1df930fb-eb7e-4e3f-bcab-15a1aa5fede0"
    }
}
```

