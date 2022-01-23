**Example 1: 为当前实例设置账号权限。**

为当前实例的指定账号设置操作权限。

Input: 

```
tccli mongodb SetAccountUserPrivilege --cli-unfold-argument  \
    --InstanceId xx \
    --UserName xx \
    --AuthRole.0.Mask 0 \
    --AuthRole.0.NameSpace xx
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

