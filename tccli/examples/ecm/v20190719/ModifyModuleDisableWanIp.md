**Example 1: 修改模块是否禁止分配外网ip**



Input: 

```
tccli ecm ModifyModuleDisableWanIp --cli-unfold-argument  \
    --ModuleId em-0vag13d1 \
    --DisableWanIp true
```

Output: 
```
{
    "Response": {
        "RequestId": "42c0f8c7-a1fb-4ba5-9e5d-fa3447331a12"
    }
}
```

