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
        "ConnectorParameter": "xx",
        "RequestId": "xx"
    }
}
```

