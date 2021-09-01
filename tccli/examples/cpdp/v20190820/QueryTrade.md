**Example 1: QueryTrade**



Input: 

```
tccli cpdp QueryTrade --cli-unfold-argument  \
    --TradeFileId tdflid20191123023
```

Output: 
```
{
    "Response": {
        "RequestId": "00b7a4d1-cdb0-412a-abfa-7d9e693f2802",
        "Result": {
            "Data": {
                "Status": "TRADE_FILE_APPROVED",
                "TradeName": "帽子",
                "PayerId": "qyfkr201911230001",
                "TradeCurrency": "USD",
                "TradeTime": "20191118",
                "PayeeName": "个人收款姓名A",
                "TradeOrderId": "tdodid20191118021",
                "FailReason": null,
                "MerchantId": "202002270000054004",
                "ServiceDetail": null,
                "TradeAmount": "10.22",
                "TradeType": "GOODS",
                "GoodsCarrier": "中外运空运;MC2410918701000931505",
                "PayeeCountryCode": "CHN",
                "ServiceTime": null,
                "TradeCount": 1,
                "TradeFileId": "tdflid20191123023"
            },
            "Code": "000000"
        }
    }
}
```

