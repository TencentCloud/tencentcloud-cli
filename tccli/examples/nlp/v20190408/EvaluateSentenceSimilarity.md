**Example 1: 句子相似度调用示例**

分析句子相似度

Input: 

```
tccli nlp EvaluateSentenceSimilarity --cli-unfold-argument  \
    --SentencePairList.0.SourceText 北京到上海的火车票 \
    --SentencePairList.0.TargetText 上海到北京的火车票 \
    --SentencePairList.1.SourceText 北京到上海的火车票 \
    --SentencePairList.1.TargetText 北京到上海的高铁票
```

Output: 
```
{
    "Response": {
        "RequestId": "fd4ea683-422a-4149-8ba8-501458bd826e",
        "ScoreList": [
            0.965566,
            0.798171
        ]
    }
}
```

