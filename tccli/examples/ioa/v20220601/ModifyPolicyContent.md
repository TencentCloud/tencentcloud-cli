**Example 1: 更新策略内容**



Input: 

```
tccli ioa ModifyPolicyContent --cli-unfold-argument  \
    --PolicyContent.0.Modify 0 \
    --PolicyContent.0.PolicyItemName ClientDLSetting \
    --PolicyContent.0.Version 1 \
    --PolicyContent.0.OSType 0 \
    --PolicyContent.0.Operation 0 \
    --PolicyContent.0.Id 474 \
    --PolicyId 474
```

Output: 
```
{
    "Response": {
        "RequestId": "99dde025-5400-4910-9028-94b7fffa40d8",
        "Data": {
            "PolicyId": 474
        }
    }
}
```

**Example 2: 创建策略项的内容**

创建策略项的内容

Input: 

```
tccli ioa ModifyPolicyContent --cli-unfold-argument  \
    --PolicyId 306968 \
    --PolicyContent.0.Operation 1 \
    --PolicyContent.0.OSType 0 \
    --PolicyContent.0.PolicyItemName ClientDLSetting \
    --PolicyContent.0.Modify 1 \
    --PolicyContent.0.Version 1 \
    --PolicyContent.0.Data {"ClientDlMode":1} \
    --PolicyContent.1.Operation 1 \
    --PolicyContent.1.OSType 0 \
    --PolicyContent.1.PolicyItemName QMUUpdateType \
    --PolicyContent.1.Modify 1 \
    --PolicyContent.1.Version 1 \
    --PolicyContent.1.Data {"Day":1,"Md5":"","Url":"","Hour":0,"Mode":1,"Enable":1,"Minute":0,"HourEnd":1,"Version":"","TimeType":2,"MinuteEnd":0}
```

Output: 
```
{
    "Response": {
        "Data": {
            "PolicyId": 306968
        },
        "RequestId": "7ca984a9-77f1-4b04-bc4e-7c6568c5207e"
    }
}
```

