**Example 1: 为当前实例设置账号权限**

为当前实例的指定账号设置操作权限

Input: 

```
tccli mongodb SetAccountUserPrivilege --cli-unfold-argument  \
    --InstanceId cmgo-9d0p6umb \
    --UserName test_user \
    --AuthRole.0.Mask 0 \
    --AuthRole.0.NameSpace eg_collection
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

