**Example 1: 查询制品详情**



Input: 

```
tccli monitor DescribeAIWorkbenchArtifact --cli-unfold-argument  \
    --ArtifactId a9***************************c86 \
    --NeedDownloadURL 1
```

Output: 
```
{
    "Response": {
        "Artifact": {
            "AgentId": "agt-fl41a45q",
            "ArtifactId": "a9b50a2ab7fd09af3ae37c6f0262cc86",
            "CreatedAt": 0,
            "IsGlobal": false,
            "MimeType": "application/json",
            "Name": "instances.json",
            "SizeBytes": 41,
            "SkillId": "skl-183na51w",
            "StoragePath": "sandbox_file://ses-n3qlvaiqqfwn/instances.json",
            "UpdatedAt": 0
        },
        "DownloadURL": "https://observability-*****************************************************************************************************************************************************************************************************************************************************************************************************************************",
        "DownloadURLExpiredAt": "2026-05-26T08:50:29Z",
        "RequestId": "8fe8e08b-a92d-4b0a-82bd-08404a3365c4"
    }
}
```

