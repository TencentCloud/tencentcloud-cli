**Example 1: Record 更新模式：移动 stable + 新增 grey**

不提交 Source/CustomDescriptors 时是 Record 更新模式，允许 Description/LabelMutations。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --LabelMutations.0.Operation SET \
    --LabelMutations.0.Name stable \
    --LabelMutations.0.VersionId rv-0002abcd \
    --LabelMutations.0.Reason 发布已验证的第二版 \
    --LabelMutations.1.Operation SET \
    --LabelMutations.1.Name grey \
    --LabelMutations.1.VersionId rv-0003abcd \
    --LabelMutations.1.Reason 灰度环境验证第三版
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Record": {
            "RecordId": "rec-0123abcd",
            "LabelSet": [
                "stable",
                "latest",
                "grey"
            ]
        }
    }
}
```

**Example 2: Version 创建模式：MCP URL_IMPORT**

提交内容输入进入 Version 创建模式；禁止同时提交 Description/LabelMutations。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionName v2 \
    --ChangeLog 增加订单状态筛选参数 \
    --MCPSource.Type URL_IMPORT \
    --MCPSource.EndpointURL https://example.com/mcp-v2.json
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Record": {
            "RecordId": "rec-0123abcd"
        },
        "Version": {
            "VersionId": "rv-0004abcd",
            "Revision": 4,
            "Status": "PENDING_APPROVAL"
        }
    }
}
```

