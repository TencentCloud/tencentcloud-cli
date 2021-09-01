**Example 1: 修改模块带宽上限**

修改模块带宽上限

Input: 

```
tccli ecm ModifyModuleNetwork --cli-unfold-argument  \
    --ModuleId em-bvr8f24q \
    --DefaultBandwidth 50
```

Output: 
```
{
    "Response": {
        "RequestId": "36c0f8c7-a1fb-4ba5-9e5d-fa3447331a5f"
    }
}
```

