**Example 1: 查看设备详情**

用于查看设备信息

Input: 

```
tccli iotexplorer DescribeDevice --cli-unfold-argument  \
    --ProductId ABCDE12345\
    --DeviceName dev01
```

Output: 
```
{
    "Response": {
        "Device": [
            {
                "DeviceName": "dev01",
                "Status": 3,
                "DevicePsk": "",
                "FirstOnlineTime": 0,
                "LoginTime": 0
            }
        ],
        "RequestId": "e020416b-bc15-4563-9afc-0e5a111a5711"
    }
}
```

