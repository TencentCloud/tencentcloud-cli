**Example 1: 上传 Skill 触发检测**



Input: 

```
tccli csip CreateSkillScan --cli-unfold-argument  \
    --FileBase64 UEsDBBQAAAAIAA... \
    --FileName my-skill.zip
```

Output: 
```
{
    "Response": {
        "ContentHash": "sha256:a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
        "EngineVersion": 20260501,
        "Status": "SCANNING",
        "Message": "File received, scan task created",
        "RequestId": "d3b7c5a1-6e4f-2d8a-9c1b-f5e3a7d2b8c6"
    }
}
```

