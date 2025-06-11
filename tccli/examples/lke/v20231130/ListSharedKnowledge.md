**Example 1: 列举共享知识库**

列举共享知识库

Input: 

```
tccli lke ListSharedKnowledge --cli-unfold-argument  \
    --Keyword 计算机 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f1c3dcb2-e3d7-686e-a809-29d53f7a915f",
        "KnowledgeList": [
            {
                "AppList": [
                    {
                        "AppBizId": "1906370579678213376",
                        "AppName": "AI助手1"
                    }
                ],
                "Knowledge": {
                    "EmbeddingModel": "general-text-embedding-v2.7",
                    "KnowledgeBizId": "1908652910168703294",
                    "KnowledgeDescription": "计算机基础理论知识库",
                    "KnowledgeName": "共享知识库1",
                    "QaExtractModel": "general-qa-extract-v1.8",
                    "UpdateTime": "1747757139"
                },
                "User": {
                    "UserBizId": "1908176109182178608",
                    "UserName": "700000963993"
                }
            }
        ],
        "Total": 1
    }
}
```

