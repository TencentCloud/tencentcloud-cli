**Example 1: 查询连接器事件匹配规则样式**

查询连接器事件匹配规则样式

Input: 

```
tccli eb ListConnectorEventPatterns --cli-unfold-argument  \
    --ConnectorType ckafka
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "EventPatterns": [
            {
                "EventName": "连接器事件",
                "EventPattern": "{\n  \"source\": \"cvm.cloud.tencent\",\n  \"type\": [\n    \"cvm:ErrorEvent:DiskReadonly\"\n  ],\n  \"subject\": [{\n    \"anything-but\": [\"ins-jy9g0ekp\",\"ins-cipufxfl\"]\n  }]\n}"
            }
        ]
    }
}
```

