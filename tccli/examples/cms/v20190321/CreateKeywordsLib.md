**Example 1: 创建关键词词库**

创建关键词词库

Input: 

```
tccli cms CreateKeywordsLib --cli-unfold-argument  \
    --UserAppID xx \
    --LibName xx \
    --UserSubUin xx \
    --Describe xx \
    --Suggestion xx \
    --UserUin xx \
    --MatchType xx \
    --Type xx
```

Output: 
```
{
    "Response": {
        "RequestId": "123123213",
        "ID": "1"
    }
}
```

**Example 2: 正常创建词库示例**

正常创建词库示例

Input: 

```
tccli cms CreateKeywordsLib --cli-unfold-argument  \
    --UserAppID 123 \
    --LibName 测试词库2 \
    --UserSubUin 123 \
    --Describe 测试词库描述 \
    --Suggestion Review \
    --UserUin 123 \
    --MatchType FuzzyMatch \
    --Type Text
```

Output: 
```
{
    "Response": {
        "ID": "4c49c04f-6617-4705-b3ff-bedce642bfcb",
        "RequestId": "a479e517-eced-426c-9568-fdd10fdc9e24"
    }
}
```

