**Example 1: 句子相似度示例**



Input: 

```
tccli nlp TextSimilarityPro --cli-unfold-argument  \
    --SrcText "北京到上海的火车票" \
    --TargetText "北京到上海的飞机票" "北京到上海的高铁票" "上海到北京的火车票"
```

Output: 
```
{
    "Response": {
        "Similarity": [
            {
                "Score": 0.9943903139727261,
                "Text": "北京到上海的飞机票"
            },
            {
                "Score": 0.9823085983303148,
                "Text": "北京到上海的高铁票"
            },
            {
                "Score": 0.6515947587356785,
                "Text": "上海到北京的火车票"
            }
        ],
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075"
    }
}
```

