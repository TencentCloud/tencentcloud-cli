**Example 1: 获取连接器操作列表**



Input: 

```
tccli eis ListEisConnectorOperations --cli-unfold-argument  \
    --ConnectorName xx \
    --ConnectorVersion xx
```

Output: 
```
{
    "Response": {
        "Operations": [
            {
                "OperationName": "xx",
                "DisplayName": "xx",
                "IsTrigger": true
            }
        ],
        "RequestId": "xx"
    }
}
```

