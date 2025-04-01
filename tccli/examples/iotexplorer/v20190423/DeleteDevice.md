**Example 1: 删除设备**

删除设备

Input: 

```
tccli iotexplorer DeleteDevice --cli-unfold-argument  \
    --ProductId KO9JAFB9W5 \
    --DeviceName dev
```

Output: 
```
{
    "Response": {
        "ResultCode": "fail",
        "ResultMessage": "device has binded family",
        "RequestId": "3edc-7ujm-89jfa"
    }
}
```

