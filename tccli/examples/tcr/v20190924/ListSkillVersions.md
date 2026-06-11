**Example 1: 查看skill 列表**



Input: 

```
tccli tcr ListSkillVersions --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --SkillName e2e-test/test-skill \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VersionList": [
            {
                "PushTime": "2026-03-23T13:28:56.172Z",
                "Size": 1445,
                "Version": "1.0.0"
            }
        ],
        "RequestId": "d614ddcb-0233-4ffb-be0a-a10252385736"
    }
}
```

