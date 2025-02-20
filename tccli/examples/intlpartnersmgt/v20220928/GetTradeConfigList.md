**Example 1: 查询行业信息**



Input: 

```
tccli intlpartnersmgt GetTradeConfigList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TradeList": [
            {
                "Id": "kghy_01",
                "Name": "农林牧渔业",
                "Children": [
                    {
                        "Id": "kghy_0101",
                        "Name": "农业",
                        "TradeInfo": "kghy_01"
                    },
                    {
                        "Id": "kghy_0102",
                        "Name": "林业",
                        "TradeInfo": "kghy_01"
                    },
                    {
                        "Id": "kghy_0103",
                        "Name": "畜牧业",
                        "TradeInfo": "kghy_01"
                    },
                    {
                        "Id": "kghy_0104",
                        "Name": "渔业",
                        "TradeInfo": "kghy_01"
                    }
                ]
            }
        ],
        "RequestId": "abc123"
    }
}
```

