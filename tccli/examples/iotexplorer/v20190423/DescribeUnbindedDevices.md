**Example 1: 获取未绑定的设备列表**



Input: 

```
tccli iotexplorer DescribeUnbindedDevices --cli-unfold-argument  \
    --ProductId 12345ABCDE \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "bec3b0f5-f994-43bf-8e99-21de4e683bfc",
        "Total": 1,
        "UnbindedDevices": [
            {
                "ProductId": "12345ABCDE",
                "DeviceName": "subdev4"
            }
        ]
    }
}
```

