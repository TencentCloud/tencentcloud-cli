**Example 1: 新建QA分类**

新建QA分类

Input: 

```
tccli lke CreateQACate --cli-unfold-argument  \
    --LoginUin 600000562455 \
    --LoginSubAccountUin 600000562455 \
    --BotBizId 1714970520775950336 \
    --ParentBizId 1733053612030808064 \
    --Name 创建QA分类
```

Output: 
```
{
    "Response": {
        "CanAdd": true,
        "CanDelete": true,
        "CanEdit": true,
        "CateBizId": "1734144647474577408",
        "RequestId": "39db6689-ceab-4ae7-87a9-f926774255d7"
    }
}
```

