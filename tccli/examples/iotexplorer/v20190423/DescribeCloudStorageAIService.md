**Example 1: 查询设备云存AI服务**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIService --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType PackageDetect
```

Output: 
```
{
    "Response": {
        "Enabled": true,
        "ROI": "{}",
        "Config": "{\"param1\":\"value1\"}",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

