**Example 1: 查询设备云存AI服务**



Input: 

```
tccli iotexplorer DescribeCloudStorageAIService --cli-unfold-argument  \
    --ProductId KH6Q8C4N0D \
    --DeviceName aaa_31400554_1 \
    --ServiceType Highlight \
    --ChannelId 0
```

Output: 
```
{
    "Response": {
        "Enabled": true,
        "ROI": "{\"param1\":\"value1\"}",
        "Config": "{\"param1\":\"value1\"}",
        "Type": 1,
        "Status": 1,
        "ExpireTime": 1719294987,
        "UserId": "user1",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

