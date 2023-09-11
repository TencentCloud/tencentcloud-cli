**Example 1: 实例手动主备切换**



Input: 

```
tccli sqlserver SwitchCloudInstanceHA --cli-unfold-argument  \
    --InstanceId mssql-987qhaha \
    --WaitSwitch 0
```

Output: 
```
{
    "Response": {
        "RequestId": "863b2797-858b-49f3-88e9-50159e564cbc",
        "FlowId": 109181
    }
}
```

