**Example 1: 查看应用引用的共享知识库列表**



Input: 

```
tccli lke ListReferShareKnowledge --cli-unfold-argument  \
    --AppBizId 1908652910168703294
```

Output: 
```
{
    "Response": {
        "RequestId": "f1c3dcb2-e3d7-686e-a809-29d53f7a915f",
        "List": [
            {
                "EmbeddingModel": "general-text-embedding-v2.7",
                "KnowledgeBizId": "1908652910168703294",
                "KnowledgeDescription": "计算机基础理论知识库",
                "KnowledgeName": "共享知识库1",
                "QaExtractModel": "general-qa-extract-v1.8",
                "UpdateTime": "1747757139"
            }
        ]
    }
}
```

