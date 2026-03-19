**Example 1: 获取Talk设备激活记录列表示例**



Input: 

```
tccli iotexplorer GetTWeTalkActiveRecordList --cli-unfold-argument  \
    --StartTime 1772014291 \
    --EndTime 1772019291 \
    --Offset 1 \
    --Limit 10 \
    --ProductId RNSEEMTZB0 \
    --DeviceName dev \
    --ServiceType 1
```

Output: 
```
{
    "Response": {
        "ActiveRecords": [
            {
                "ActiveTime": 1772015290,
                "DeviceName": "dev",
                "ErrorMsg": "",
                "ExpireTime": 11238941496,
                "ProductId": "RNSEEMTZB0",
                "ServiceType": 1,
                "Status": 1
            }
        ],
        "Total": 283,
        "RequestId": "3f8b798b-a251-4936-841d-663efb7ac099"
    }
}
```

