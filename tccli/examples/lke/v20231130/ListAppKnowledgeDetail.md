**Example 1: 列表查询知识库容量详情**

列表查询知识库容量详情

Input: 

```
tccli lke ListAppKnowledgeDetail --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "94d7732a-0b85-45a8-9f3f-2c73e750ba67",
        "Total": 6
    }
}
```

**Example 2: 列表查询应用知识库容量使用详情**

列表查询应用知识库容量使用详情

Input: 

```
tccli lke ListAppKnowledgeDetail --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "99007a19-557c-43ec-9bdc-2f8587b461cf",
        "Total": 0
    }
}
```

