**Example 1: 创建 MANUAL 审批的 Registry**

响应体带 RequestId 与 RegistryId；后续获取详情用 DescribeRegistry。ApprovalMode 省略时默认 AUTO。

Input: 

```
tccli ags CreateRegistry --cli-unfold-argument  \
    --Name example-registry \
    --Description 对外提供实时天气 MCP/Agent 资产。 \
    --ApprovalMode MANUAL
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "RegistryId": "reg-0123abcd",
        "Registry": {
            "RegistryId": "reg-0123abcd",
            "Name": "example-registry",
            "Description": "AGS 示例 Registry",
            "ApprovalMode": "MANUAL",
            "Region": "ap-guangzhou",
            "Status": "ACTIVE",
            "AppId": 1300000000,
            "CreatorUin": "100000000001",
            "CreatorSubAccountUin": "",
            "RecordCount": 0,
            "PublishedRecordCount": 0,
            "CreateTime": "2026-08-11T10:00:00Z",
            "UpdateTime": "2026-08-11T10:00:00Z",
            "Tags": []
        }
    }
}
```

