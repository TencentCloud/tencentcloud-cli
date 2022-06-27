**Example 1: 查询对账单分页数据成功示例**

查询对账单分页数据成功示例

Input: 

```
tccli cpdp QueryOpenBankBillDataPage --cli-unfold-argument  \
    --ChannelMerchantId CM614829654947741696 \
    --BillDate 2022-05-20 \
    --ChannelName HELIPAY \
    --PageNo 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "431712c3-4c1e-4028-921a-ccb4df715f23",
        "Result": {
            "PageNo": 1,
            "PageSize": 10,
            "Count": 1,
            "DataList": [
                {
                    "BillDate": "2022-05-20",
                    "Channel": "HELIPAY",
                    "SubChannel": "",
                    "ParentMerchantId": "",
                    "OutMerchantId": "",
                    "MerchantId": "CM615222155219103744",
                    "EndMerchantId": "",
                    "OutTradeNo": "test21212328671312312112",
                    "TradeNo": "614841264310980609",
                    "EndTradeNo": "22052015010525635420411",
                    "PaymentType": "payment",
                    "BusinessType": "PAY",
                    "TradeTime": "2022-05-24 15:19:41",
                    "FinishTime": "2022-05-20 15:19:40",
                    "TradeStatus": "1",
                    "CheckStatus": "1",
                    "CheckFailReason": "",
                    "OrderAmount": "0.03",
                    "ServiceFee": "0.00",
                    "PayeeAccount": "",
                    "PayeeName": "",
                    "PayerAccount": "",
                    "PayerName": "",
                    "Description": "成功"
                }
            ]
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

