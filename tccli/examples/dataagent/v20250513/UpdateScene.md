**Example 1: 示例**

示例

Input: 

```
tccli dataagent UpdateScene --cli-unfold-argument  \
    --InstanceId instance001 \
    --Scene.SceneId sn001 \
    --Scene.SceneName sn_cran \
    --Scene.Skills rag \
    --Scene.Prompt keyword \
    --Scene.SearchConfig.Type 1 \
    --Scene.SearchConfig.Num 100 \
    --Scene.SearchConfig.EmbeddingWeight 0.3 \
    --Scene.SearchConfig.Rerank 1 \
    --Scene.SearchConfig.AutoRag 1 \
    --Scene.SearchConfig.KnowledgeBaseIds kb002 \
    --Scene.ExampleQAList.0.ExampleId e002 \
    --Scene.ExampleQAList.0.Questions where? \
    --Scene.ExampleQAList.0.Answer home \
    --Scene.ExampleQAList.0.Type fd \
    --Scene.CreateTime 2025-11-03 12:12:12 \
    --Scene.UpdateTime 2025-11-03 12:12:12
```

Output: 
```
{
    "Response": {
        "RequestId": "f618ef45-6b04-4fdd-b2db-ece2289d290f"
    }
}
```

