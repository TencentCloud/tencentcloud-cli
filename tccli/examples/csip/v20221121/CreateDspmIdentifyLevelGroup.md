**Example 1: 创建dspm数据识别分级组**



Input: 

```
tccli csip CreateDspmIdentifyLevelGroup --cli-unfold-argument  \
    --Name 自定义级别03 \
    --MemberId mem-23d21edw \
    --Description 级别描述 \
    --LevelItems.0.LevelName 高 \
    --LevelItems.0.LevelScore 10
```

Output: 
```
{
    "Response": {
        "Id": 7,
        "RequestId": "2e0ce520-010b-4491-beea-58e3b37b3b1d"
    }
}
```

