**Example 1: 导入一个视频到知识库中**



Input: 

```
tccli vod ImportMediaKnowledge --cli-unfold-argument  \
    --SubAppId 220885 \
    --FileId 9****************9 \
    --Definition 100 \
    --KnowledgeBaseIds kb-**********
```

Output: 
```
{
    "Response": {
        "TaskId": "220885-ImportMediaKnowledge-f178c3c17d22cb5ae56721edb396646et",
        "RequestId": "2f835f37-deca-4a35-8eef-ff73cf6040c2"
    }
}
```

