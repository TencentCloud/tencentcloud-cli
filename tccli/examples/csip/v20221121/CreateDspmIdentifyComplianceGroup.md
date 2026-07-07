**Example 1: 创建dspm数据识别模板**



Input: 

```
tccli csip CreateDspmIdentifyComplianceGroup --cli-unfold-argument  \
    --Name kyrie测试 \
    --MemberId mem-23ed1ewd \
    --Description kyrie描述 \
    --LevelGroupId 1 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Id": 10000,
        "RequestId": "cfca9e29-4405-46ea-a240-d5e2ef55d8ff"
    }
}
```

