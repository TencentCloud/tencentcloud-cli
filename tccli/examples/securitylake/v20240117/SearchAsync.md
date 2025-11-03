**Example 1: 示例**

异步检索数据

Input: 

```
tccli securitylake SearchAsync --cli-unfold-argument  \
    --Limit 3000 \
    --SearchContent U0VMRUNUICogRlJPTSB0Y20uX3NlY3VyaXR5X2xvZyBXSEVSRSBzb3VyY2V0eXBlID0neXVqaWVfaW9jX2FsZXJ0Jw== \
    --TimeValue now-3d,now \
    --SdlId sdl-free0224
```

Output: 
```
{
    "Response": {
        "RequestId": "c2b2e53a-3f48-443c-8533-aa5b49ee8fdd",
        "TaskId": "51e776b5-a3d8-43eb-8345-089d82d203e9"
    }
}
```

