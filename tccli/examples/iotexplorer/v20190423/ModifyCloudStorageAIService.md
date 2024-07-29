**Example 1: 修改云存AI服务启用状态**



Input: 

```
tccli iotexplorer ModifyCloudStorageAIService --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType Highlight \
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

**Example 2: 修改云存AI服务配置参数**



Input: 

```
tccli iotexplorer ModifyCloudStorageAIService --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType Highlight \
    --Config {"param1":"value1"}
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

