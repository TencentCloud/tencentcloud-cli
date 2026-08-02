**Example 1: 修改知识库的名称和描述**



Input: 

```
tccli vod ModifyKnowledgeBase --cli-unfold-argument  \
    --SubAppId 200000 \
    --KnowledgeBaseId kb-********** \
    --Name 新的名字 \
    --Description 这是新的描述
```

Output: 
```
{
    "Response": {
        "RequestId": "17599a3b-5006-46fa-bc0a-a97b1360bf7b"
    }
}
```

