**Example 1: 聚鑫-查询退款**



Input: 

```
tccli cpdp QueryCloudRefundOrder --cli-unfold-argument  \
    --MidasEnvironment sandbox \
    --MidasAppId demo001 \
    --UserId 66661877211 \
    --RefundId 545464656565656122
```

Output: 
```
{
    "Response": {
        "ChannelExternalOrderId": "4200001369202204124504975386",
        "CurrencyType": "CNY",
        "ChannelOrderId": "202204120001300008",
        "TotalRefundAmt": 500,
        "ChannelExternalRefundId": "50300201302022041319287908513",
        "SubRefundList": [
            {
                "ChannelSubOrderId": "202204120001300009",
                "SubOutTradeNo": "4805X1183110364415535792X",
                "ChannelExternalOrderId": "",
                "SubAppId": "",
                "RefundAmt": 500,
                "ChannelSubRefundId": "545464656565656122",
                "SubRefundId": "545464656565656122",
                "ChannelExternalRefundId": ""
            }
        ],
        "RefundId": "545464656565656122",
        "UsedRefundId": "545464656565656122",
        "RequestId": "c34493c8-5d0d-4ee0-8ab0-369330691c1f",
        "Metadata": "",
        "AppId": "",
        "OutTradeNo": "1183110364214208944",
        "ChannelRefundId": "545464656565656122",
        "State": "2"
    }
}
```

