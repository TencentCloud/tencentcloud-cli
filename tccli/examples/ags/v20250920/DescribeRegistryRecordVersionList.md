**Example 1: 市场模式按 Harness 配对筛选**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags DescribeRegistryRecordVersionList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name label \
    --Filters.0.Values stable \
    --Filters.1.Name descriptor_type \
    --Filters.1.Values PLUGIN \
    --Filters.2.Name supported_harness_engine \
    --Filters.2.Values pi \
    --Filters.3.Name supported_harness_version \
    --Filters.3.Values 1.3.0 \
    --Filters.4.Name metadata.publisher \
    --Filters.4.Values 示例发布者 \
    --RegistryId MARKETPLACE
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "VersionSet": [
            {
                "VersionId": "rv-0123abcd",
                "RecordId": "rec-0123abcd",
                "Revision": 1,
                "VersionName": "1.0.0",
                "ChangeLog": "首次发布",
                "Descriptors": "{\"name\": \"example-plugin\", \"description\": \"示例 Plugin 文件资产\"}",
                "Status": "APPROVED",
                "LabelSet": [
                    "latest",
                    "stable"
                ],
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
                "CreateTime": "2030-01-01T00:00:00Z",
                "UpdateTime": "2030-01-01T00:00:00Z",
                "ContentStatus": "READY",
                "ContentSHA256": "2d711642b726b04401627ca9fbac32f5c8530fb1903cc4db02258717921a4881",
                "ContentSizeBytes": 1,
                "ContentReadyTime": "2030-01-01T00:00:00Z",
                "Name": "example-plugin",
                "Description": "示例 Plugin 文件资产",
                "DescriptorType": "PLUGIN"
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 普通模式按 Harness 配对筛选**

参数示意；资源 ID、账号、时间、摘要及 example.com URL 为示例，不对应真实资源，请替换后调用。

Input: 

```
tccli ags DescribeRegistryRecordVersionList --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name supported_harness_engine \
    --Filters.0.Values pi \
    --Filters.1.Name supported_harness_version \
    --Filters.1.Values 1.3.0 \
    --Filters.2.Name metadata.publisher \
    --Filters.2.Values 示例发布者
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "VersionSet": [
            {
                "VersionId": "rv-0123abcd",
                "RecordId": "rec-0123abcd",
                "Revision": 1,
                "VersionName": "1.0.0",
                "ChangeLog": "首次发布",
                "Descriptors": "{\"name\": \"example-plugin\", \"description\": \"示例 Plugin 文件资产\"}",
                "SourceType": "FILE",
                "SourceConfig": "{\"Type\":\"FILE\",\"SizeBytes\":1}",
                "Status": "APPROVED",
                "ApprovalMode": "MANUAL",
                "ConfigSHA256": "8eb0ce58a4b47f2d9f4154cfe67815d4977b99abdfd35d735219b1d5a5436526",
                "LabelSet": [
                    "latest",
                    "stable"
                ],
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
                "ContentReadyTime": "2030-01-01T00:00:00Z",
                "Name": "example-plugin",
                "Description": "示例 Plugin 文件资产",
                "DescriptorType": "PLUGIN"
            }
        ],
        "TotalCount": 1
    }
}
```

