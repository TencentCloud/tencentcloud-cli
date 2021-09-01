**Example 1: 获取连接器配置参数**



Input: 

```
tccli eis DescribeEisConnectorConfig --cli-unfold-argument  \
    --ConnectorName xx \
    --ConnectorVersion xx
```

Output: 
```
{
    "Response": {
        "ConnectorParameter": "{\"attributes\":{\"apiType\":\"XML\",\"apiVersion\":\"1.0.0\",\"description\":\"集成腾讯乐享通讯录管理等API\",\"displayName\":\"腾讯乐享\",\"expressionType\":\"dataway\",\"expressionVersion\":\"1.0.0\",\"name\":\"tencent-lexiang\",\"version\":\"1.0.0\"},\"properties\":[{\"attributes\":{\"displayName\":\"授权类型\",\"name\":\"grant_type\",\"required\":\"false\",\"type\":\"string\"}},{\"attributes\":{\"displayName\":\"开发者ID\",\"name\":\"app_key\",\"required\":\"true\",\"type\":\"string\"}},{\"attributes\":{\"displayName\":\"开发者secret\",\"name\":\"app_secret\",\"required\":\"true\",\"type\":\"string\"}}]}",
        "RequestId": "s1621938120801752507"
    }
}
```

