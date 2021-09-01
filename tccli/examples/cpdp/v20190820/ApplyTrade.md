**Example 1: ApplyTrade**



Input: 

```
tccli cpdp ApplyTrade --cli-unfold-argument  \
    --TradeFileId tdflid20191123023 \
    --TradeOrderId tdodid20191118021 \
    --PayerId qyfkr201911230001 \
    --PayeeName 个人收款 \
    --PayeeCountryCode CHN \
    --TradeType GOODS \
    --TradeTime 20191118 \
    --TradeCurrency USD \
    --TradeAmount 10.22 \
    --TradeName 帽子 \
    --TradeCount 1 \
    --GoodsCarrier 中外运空运;MC2410918701000931505
```

Output: 
```
{
    "Response": {
        "RequestId": "740cb348-9ae0-4a40-a9eb-88b3c7425774",
        "Result": {
            "Data": {
                "Status": "TRADE_FILE_APPROVED",
                "PayerId": "qyfkr201911230001",
                "TradeCurrency": "USD",
                "TradeAmount": "10.22",
                "MerchantId": "202002270000054004",
                "TradeFileId": "tdflid20191123023"
            },
            "Code": "000000"
        }
    }
}
```

