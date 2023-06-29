**Example 1: 查询连接器列表**

查询连接器列表

Input: 

```
tccli eb ListConnectors --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ffd4aae2-c29e-40a8-b18c-037a17ed810c",
        "Connectors": [
            {
                "ConnectorName": "kafka连接器",
                "ConnectorType": "ckafka"
            }
        ]
    }
}
```

