**Example 1: 更新词库**



Input: 

```
tccli cms ModifyKeywordsLib --cli-unfold-argument  \
    --UserAppID xx \
    --UserUin xx \
    --Fields.0.Name xx \
    --Fields.0.Value xx \
    --ID xx \
    --UserSubUin xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 2: 正常修改词库名称**



Input: 

```
tccli cms ModifyKeywordsLib --cli-unfold-argument  \
    --UserUin 123 \
    --UserSubUin 123 \
    --UserAppID 123 \
    --ID 4c49c04f-6617-4705-b3ff-bedce642bfcb \
    --Fields.0.Name LibName \
    --Fields.0.Value 修改后的词库名称
```

Output: 
```
{
    "Response": {
        "RequestId": "db6efd42-5472-4606-9dc3-3848d8e641bf"
    }
}
```

