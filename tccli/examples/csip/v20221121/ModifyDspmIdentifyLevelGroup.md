**Example 1: ModifyDspmIdentifyLevelGroup**



Input: 

```
tccli csip ModifyDspmIdentifyLevelGroup --cli-unfold-argument  \
    --Id 7 \
    --Name 修改分级组 \
    --MemberId mem-012dass1 \
    --Description 修改分级组描述 \
    --LevelItems.0.LevelName S1 \
    --LevelItems.0.LevelScore 10
```

Output: 
```
{
    "Response": {
        "RequestId": "20952437-2bbe-44ca-95c8-3160e268df6b"
    }
}
```

