**Example 1: 句子相似度调用示例**

分析句子相似度

Input: 

```
tccli nlp EvaluateSentenceSimilarity --cli-unfold-argument  \
    --SentencePairList.0.SourceText 北京到上海的火车票 \
    --SentencePairList.0.TargetText 上海到北京的火车票
```

Output: 
```
{
    "Response": {
        "RequestId": "d37e6fc7-aa12-42e4-b68a-e74dbe7548cb",
        "ScoreList": [
            0.903129852566213
        ]
    }
}
```

