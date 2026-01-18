**Example 1: 示例**

示例

Input: 

```
tccli dataagent QuerySceneList --cli-unfold-argument  \
    --InstanceId instance001 \
    --SceneId s001 \
    --SceneName sn001 \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "Datas": [
            {
                "ExampleQAList": [
                    {
                        "Answer": "1",
                        "ExampleId": "1",
                        "Questions": [
                            "1"
                        ],
                        "Type": ""
                    }
                ],
                "Prompt": "testkeyword",
                "SceneId": "1",
                "SceneName": "1",
                "SearchConfig": {
                    "EmbeddingWeight": 0.5,
                    "KnowledgeBaseIds": [
                        "klbase-1234567890"
                    ],
                    "Num": 10,
                    "Rerank": 1,
                    "Type": 1
                },
                "Skills": [
                    "rag",
                    "data_analytics"
                ]
            }
        ],
        "RequestId": "4b54d5f7-c23b-4227-9589-57cab0d95f27"
    }
}
```

