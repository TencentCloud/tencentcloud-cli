**Example 1: 创建 CUSTOM 类型 Record**

CUSTOM 直接提交顶层 CustomDescriptors；服务端 SourceType 固定为 MANUAL。

Input: 

```
tccli ags CreateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --Name custom-order-query \
    --DescriptorType CUSTOM \
    --CustomDescriptors {"vendor":"example","capability":"order-query"}
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "RecordId": "rec-01234567",
        "Record": {
            "RecordId": "rec-01234567",
            "DescriptorType": "CUSTOM"
        },
        "Version": {
            "VersionId": "rv-01234567",
            "Revision": 1,
            "Status": "PENDING_APPROVAL"
        }
    }
}
```

**Example 2: 创建 URL_IMPORT 类型的 MCP Record**

统一 Create 接口，通过 DescriptorType + Source Union 选择协议类型。

Input: 

```
tccli ags CreateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --Name order-query \
    --Description 订单查询 MCP 服务 \
    --DescriptorType MCP \
    --VersionName v1 \
    --MCPSource.Type URL_IMPORT \
    --MCPSource.EndpointURL https://example.com/mcp.json
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "RecordId": "rec-0123abcd",
        "Record": {
            "RecordId": "rec-0123abcd",
            "Name": "order-query",
            "DescriptorType": "MCP"
        },
        "Version": {
            "VersionId": "rv-0123abcd",
            "Revision": 1,
            "Status": "PENDING_APPROVAL"
        }
    }
}
```

