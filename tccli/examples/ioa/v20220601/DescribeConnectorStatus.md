**Example 1: 获取专线联通状态**

控制台点击刷新获取指定的连接器联通性状态

Input: 

```
tccli ioa DescribeConnectorStatus --cli-unfold-argument  \
    --ConnectorId 2kfasd9u2edb2u8a211 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsActive": true
        },
        "RequestId": "11222"
    }
}
```

