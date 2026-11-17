**Example 1: 创建 MCP URL_IMPORT 版本**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags CreateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --Name example-mcp \
    --Description 示例 MCP 服务 \
    --DescriptorType MCP \
    --VersionName 1.0.0 \
    --MCPSource.Type URL_IMPORT \
    --MCPSource.EndpointURL https://example.com/mcp \
    --Metadata.0.Name publisher \
    --Metadata.0.Value 示例发布者
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "RecordId": "rec-0123abcd",
        "Record": {
            "RecordId": "rec-0123abcd"
        },
        "Version": {
            "VersionId": "rv-0123abcd",
            "Revision": 1,
            "Status": "PENDING_APPROVAL",
            "SupportedHarnessVersions": [],
            "Metadata": [
                {
                    "Name": "publisher",
                    "Value": "示例发布者"
                }
            ]
        }
    }
}
```

**Example 2: 创建 Plugin 文件版本**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags CreateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --Name example-plugin \
    --Description 示例 Plugin 文件资产 \
    --DescriptorType PLUGIN \
    --VersionName 1.0.0 \
    --FileSource.Type FILE \
    --FileSource.SizeBytes 1 \
    --SupportedHarnessVersions.0.HarnessEngine pi \
    --SupportedHarnessVersions.0.HarnessEngineVersion 1.3.0 \
    --Metadata.0.Name publisher \
    --Metadata.0.Value 示例发布者
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "RecordId": "rec-0123abcd",
        "Record": {
            "RecordId": "rec-0123abcd",
            "RegistryId": "reg-0123abcd",
            "Name": "example-plugin",
            "Description": "示例 Plugin 文件资产",
            "DescriptorType": "PLUGIN",
            "LifecycleStatus": "ACTIVE",
            "AppId": 1250000000,
            "CreatorUin": "100000000001",
            "CreatorSubAccountUin": "100000000002",
            "VersionCount": 1,
            "LabelSet": [
                "latest"
            ],
            "CreateTime": "2030-01-01T00:00:00Z",
            "UpdateTime": "2030-01-01T00:00:00Z"
        },
        "Version": {
            "VersionId": "rv-0123abcd",
            "RecordId": "rec-0123abcd",
            "Revision": 1,
            "VersionName": "1.0.0",
            "ChangeLog": "首次发布",
            "Descriptors": "{\"name\": \"example-plugin\", \"description\": \"示例 Plugin 文件资产\"}",
            "SourceType": "FILE",
            "SourceConfig": "{\"Type\":\"FILE\",\"SizeBytes\":1}",
            "Status": "PREPARING",
            "ApprovalMode": "MANUAL",
            "ConfigSHA256": "",
            "LabelSet": [],
            "SupportedHarnessVersions": [
                {
                    "HarnessEngine": "pi",
                    "HarnessEngineVersion": "1.3.0"
                }
            ],
            "Metadata": [
                {
                    "Name": "publisher",
                    "Value": "示例发布者"
                }
            ],
            "AppId": 1250000000,
            "CreatorUin": "100000000001",
            "CreatorSubAccountUin": "100000000002",
            "CreateTime": "2030-01-01T00:00:00Z",
            "UpdateTime": "2030-01-01T00:00:00Z",
            "ContentStatus": "UPLOADING"
        },
        "ContentStatus": "UPLOADING",
        "UploadURL": "https://example.com/uploads/example-plugin.bin?signature=example",
        "ExpireTime": "2030-01-01T00:15:00Z"
    }
}
```

