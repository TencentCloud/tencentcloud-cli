**Example 1: 获取设备资源列表**



Input: 

```
tccli iotcloud DescribeDeviceResources --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --Offset 0 \
    --Limit 10 \
    --DeviceName test \
    --StartTime xxx \
    --EndTime xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Result": [
            {
                "Name": "xx",
                "ProductName": "xx",
                "Md5": "xx",
                "DeviceName": "xx",
                "ProductID": "xx",
                "UpdateTime": "xx",
                "Size": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

