**Example 1: 创建 CUSTOM 类型 Record**

CUSTOM 直接提交顶层 CustomDescriptors；服务端 SourceType 固定为 MANUAL。

Input: 

```
tccli ags CreateRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

**Example 2: 创建 URL_IMPORT 类型的 MCP Record**

统一 Create 接口，通过 DescriptorType + Source Union 选择协议类型。

Input: 

```
tccli ags CreateRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

