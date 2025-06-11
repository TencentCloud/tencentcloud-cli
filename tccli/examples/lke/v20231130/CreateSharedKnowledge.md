**Example 1: 创建共享知识库**

创建共享知识库

Input: 

```
tccli lke CreateSharedKnowledge --cli-unfold-argument  \
    --KnowledgeName 共享知识库1 \
    --KnowledgeDescription 计算机基础理论知识库 \
    --EmbeddingModel general-text-embedding-v2.7
```

Output: 
```
{
    "Response": {
        "KnowledgeBizId": "1908652910168703294",
        "RequestId": "798dbcd5-80e1-277d-aeb7-0018abab7686"
    }
}
```

