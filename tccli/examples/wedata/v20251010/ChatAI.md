**Example 1: 智能问数请求**

简单智能问数

Input: 

```
tccli wedata ChatAI --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360 \
    --DialogueKey  \
    --TaskKey  \
    --AppType CHAT_BI \
    --ChatType CHAT_QUERY_DATA \
    --Query 查询电影数量 \
    --Data {"regenerate":true,"timeRange":"thisMonth"} \
    --IsStream True
```

Output: 
```
{}
```

