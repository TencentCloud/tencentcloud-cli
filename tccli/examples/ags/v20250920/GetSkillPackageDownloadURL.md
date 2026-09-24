**Example 1: 按 Label 下载 Skill 包**

VersionId 与 Label 互斥；均省略时使用 Stable。

Input: 

```
tccli ags GetSkillPackageDownloadURL --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Label stable
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "DownloadURL": "https://cos.example/download",
        "ExpireTime": "2026-08-10T00:05:00Z",
        "SHA256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "ResolvedVersionId": "rv-0123abcd"
    }
}
```

