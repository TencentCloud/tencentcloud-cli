**Example 1: 聚鑫-查询第三方渠道数据**



Input: 

```
tccli cpdp QueryCloudChannelData --cli-unfold-argument  \
    --MidasEnvironment sandbox \
    --MidasAppId demo001 \
    --ChannelOrderId 202204120001300008 \
    --OutOrderNo 1183110364214208944 \
    --ExternalChannelDataType PAYMENT \
    --Channel wechat
```

Output: 
```
{
    "Response": {
        "OutOrderNo": "1183110364214208944",
        "ChannelOrderId": "202204120001300008",
        "ExternalChannelDataType": "PAYMENT",
        "SubAppId": "",
        "AppId": "demo001",
        "RequestId": "9a4fdad2-e1ef-408c-91da-2623b8658858",
        "ExternalChannelDataList": [
            {
                "ExternalChannelDataValue": "xxx",
                "ExternalChannelDataName": "PAYMENT_ORDER_EXTERNAL_NOTIFY_DATA"
            },
            {
                "ExternalChannelDataValue": "yyy",
                "ExternalChannelDataName": "PAYMENT_ORDER_EXTERNAL_RESPONSE_DATA"
            },
            {
                "ExternalChannelDataValue": "zzz",
                "ExternalChannelDataName": "PAYMENT_ORDER_EXTERNAL_REQUEST_DATA"
            }
        ],
        "Channel": "wechat"
    }
}
```

