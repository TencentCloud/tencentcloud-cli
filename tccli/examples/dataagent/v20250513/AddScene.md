**Example 1: 示例**

示例

Input: 

```
tccli dataagent AddScene --cli-unfold-argument  \
    --InstanceId instance001 \
    --Scene.SceneName sn0010 \
    --Scene.Skills rag \
    --Scene.Prompt keyword \
    --Scene.SearchConfig.Type 1 \
    --Scene.SearchConfig.Num 100 \
    --Scene.SearchConfig.EmbeddingWeight 0.5 \
    --Scene.SearchConfig.Rerank 1 \
    --Scene.SearchConfig.AutoRag 1 \
    --Scene.SearchConfig.KnowledgeBaseIds kb001 \
    --Scene.ExampleQAList.0.ExampleId e001 \
    --Scene.ExampleQAList.0.Questions who? \
    --Scene.ExampleQAList.0.Answer cran \
    --Scene.ExampleQAList.0.Type dfs \
    --Scene.CreateTime 2025-11-02 12:12:12 \
    --Scene.UpdateTime 2025-11-02 12:12:12
```

Output: 
```
{
    "Response": {
        "RequestId": "699ecd6f-2fbc-4d28-8dd0-683c8c0e9673",
        "SceneId": "sn001"
    }
}
```

