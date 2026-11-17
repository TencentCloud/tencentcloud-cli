**Example 1: 创建 MCP URL_IMPORT 后续版本**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionName 1.1.0 \
    --ChangeLog 更新 MCP 接入地址 \
    --MCPSource.Type URL_IMPORT \
    --MCPSource.EndpointURL https://example.com/mcp-v2 \
    --Metadata.0.Name publisher \
    --Metadata.0.Value 示例发布者
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "Record": {
            "RecordId": "rec-0123abcd"
        },
        "Version": {
            "VersionId": "rv-89abcdef",
            "Revision": 2,
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

**Example 2: 复用 Plugin 文件创建新版本**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionName 1.1.0 \
    --ChangeLog 更新兼容声明并复用文件 \
    --FileSource.Type VERSION \
    --FileSource.SourceVersionId rv-0123abcd \
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
            "VersionCount": 2,
            "LabelSet": [
                "latest"
            ],
            "CreateTime": "2030-01-01T00:00:00Z",
            "UpdateTime": "2030-01-01T00:00:00Z"
        },
        "Version": {
            "VersionId": "rv-89abcdef",
            "RecordId": "rec-0123abcd",
            "Revision": 2,
            "VersionName": "1.1.0",
            "ChangeLog": "更新兼容声明并复用文件",
            "Descriptors": "{\"name\": \"example-plugin\", \"description\": \"示例 Plugin 文件资产\"}",
            "SourceType": "FILE",
            "SourceConfig": "{\"Type\":\"FILE\",\"SizeBytes\":1}",
            "Status": "PENDING_APPROVAL",
            "ApprovalMode": "MANUAL",
            "ConfigSHA256": "8eb0ce58a4b47f2d9f4154cfe67815d4977b99abdfd35d735219b1d5a5436526",
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
            "ContentStatus": "READY",
            "ContentSHA256": "2d711642b726b04401627ca9fbac32f5c8530fb1903cc4db02258717921a4881",
            "ContentSizeBytes": 1,
            "ContentReadyTime": "2030-01-01T00:00:00Z"
        },
        "ContentStatus": "READY"
    }
}
```

**Example 3: 移动 stable Label**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --LabelMutations.0.Operation SET \
    --LabelMutations.0.Name stable \
    --LabelMutations.0.VersionId rv-0123abcd \
    --LabelMutations.0.Reason 发布已验证版本
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
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
                "latest",
                "stable"
            ],
            "CreateTime": "2030-01-01T00:00:00Z",
            "UpdateTime": "2030-01-01T00:00:00Z"
        }
    }
}
```

