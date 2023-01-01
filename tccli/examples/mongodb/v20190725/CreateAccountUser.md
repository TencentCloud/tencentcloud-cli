**Example 1: 创建mongodb实例账号**



Input: 

```
tccli mongodb CreateAccountUser --cli-unfold-argument  \
    --UserName xx \
    --InstanceId xx \
    --AuthRole.0.Mask 0 \
    --AuthRole.0.NameSpace xx \
    --UserDesc xx \
    --MongoUserPassword xx \
    --Password xx
```

Output: 
```
{
    "Response": {
        "FlowId": 1,
        "RequestId": "xx"
    }
}
```

