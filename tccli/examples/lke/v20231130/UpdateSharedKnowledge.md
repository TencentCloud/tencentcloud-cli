**Example 1: 更新共享知识库**

更新共享知识库

Input: 

```
tccli lke UpdateSharedKnowledge --cli-unfold-argument  \
    --KnowledgeBizId 1908652910168703294 \
    --Info.EmbeddingModel general-text-embedding-v2.7 \
    --Info.KnowledgeDescription 计算机基础理论知识库 \
    --Info.KnowledgeName 共享知识库1 \
    --Info.QaExtractModel general-qa-extract-v1.8
```

Output: 
```
{
    "Response": {
        "RequestId": "f1c3dcb2-e3d7-686e-a809-29d53f7a915f",
        "KnowledgeBizId": "1908652910168703294"
    }
}
```

