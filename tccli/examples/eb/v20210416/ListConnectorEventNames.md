**Example 1: 查询连接器事件中文名称**

查询连接器事件中文名称

Input: 

```
tccli eb ListConnectorEventNames --cli-unfold-argument  \
    --ConnectorType ckafka
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "EventNames": [
            {
                "EventName": "kafka连接器模版",
                "EventType": "connector:apigw"
            }
        ]
    }
}
```

