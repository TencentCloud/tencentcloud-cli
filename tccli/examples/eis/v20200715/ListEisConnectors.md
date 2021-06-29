**Example 1: 获取已上架连接器列表（最新版本）**



Input: 

```
tccli eis ListEisConnectors --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Connectors": [
            {
                "Company": "",
                "ConnectorName": "tencent-lexiang",
                "ConnectorVersion": "1.0.0",
                "CreateTime": 1621684293,
                "DisplayName": "腾讯乐享",
                "Product": ""
            }
        ],
        "RequestId": "s1621939791738929666",
        "TotalCount": 1
    }
}
```

