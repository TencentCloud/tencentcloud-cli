**Example 1: DataAgent问答**

DataAgent问答

Input: 

```
tccli dataagent ChatAI --cli-unfold-argument  \
    --InstanceId dataagent-hLhMpd0H \
    --SessionId cabb4c9c-4c4f-45c9-94fc-b3061e503176 \
    --Model hunyuan \
    --Question what are you doing ? \
    --DeepThinking True \
    --Context {"KnowledgeBases":[{"KnowledgeBaseId":"klbase-kSnxNtvrXI","FileIds":[],"Databases":[{"MCP":{"DataSourceId":"datasource_tchoused_example"},"DbTables":[]}]}],"WhiteList":[]}
```

Output: 
```
{
    "v": "I'm here and ready to assist you with any data-related questions or tasks you might have!"
}
```

