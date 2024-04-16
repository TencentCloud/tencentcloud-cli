**Example 1: 修改设备云存AI服务开通状态**



Input: 

```
tccli iotexplorer ModifyCloudStorageAIService --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType PackageDetect \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

