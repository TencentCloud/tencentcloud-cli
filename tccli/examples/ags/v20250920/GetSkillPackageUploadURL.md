**Example 1: 重试 Skill Version 上传**



Input: 

```
tccli ags GetSkillPackageUploadURL --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionId rv-0123abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "UploadURL": "https://cos.example/upload",
        "ContentStatus": "UPLOADING"
    }
}
```

