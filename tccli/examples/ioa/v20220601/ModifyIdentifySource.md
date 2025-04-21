**Example 1: 示例1**

编辑身份源配置

Input: 

```
tccli ioa ModifyIdentifySource --cli-unfold-argument  \
    --Id  \
    --Type  \
    --Name  \
    --Config  \
    --ExtraConfig  \
    --SyncEnable True \
    --SyncPolicy  \
    --SyncPolicyParams 
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "",
            "Name": "",
            "Type": "",
            "TypeForIoa": 1,
            "Config": "",
            "ExtraConfig": "",
            "SyncEnable": true,
            "SyncPolicy": "",
            "SyncPolicyParams": "",
            "PresentInfo": [
                {
                    "Name": "",
                    "Value": ""
                }
            ],
            "CreateTime": "",
            "UpdateTime": ""
        },
        "RequestId": "81d13817-209e-4237-978e-71ec82fe2c77"
    }
}
```

