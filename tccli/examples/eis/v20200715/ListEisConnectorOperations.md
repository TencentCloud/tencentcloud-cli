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
                "DisplayName": "更新成员",
                "IsTrigger": false,
                "OperationName": "update-user"
            },
            {
                "DisplayName": "删除成员",
                "IsTrigger": false,
                "OperationName": "resign-user"
            }
        ],
        "RequestId": "s1621939905452658979"
    }
}
```

