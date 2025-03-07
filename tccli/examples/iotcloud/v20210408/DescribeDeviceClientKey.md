**Example 1: 获取设备密钥**



Input: 

```
tccli iotcloud DescribeDeviceClientKey --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --DeviceName dev-001
```

Output: 
```
{
    "Response": {
        "ClientKey": "----------BEGIN PRIVATE KEY-----\nIIDS...Fw==\n-----END PRIVATE KEY-----\n",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

