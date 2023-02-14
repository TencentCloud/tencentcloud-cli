**Example 1: 词向量示例**

特别说明：为方便观看，如下示例中，向量维度仅显示10维。实际维度以原API说明为准。

Input: 

```
tccli nlp WordEmbedding --cli-unfold-argument  \
    --Text 自然语言处理
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075",
        "Dimension": 10,
        "Vector": [
            0.0723935,
            0.138519,
            0.0297711,
            0.0160847,
            0.0354727,
            0.0133147,
            0.0901527,
            0.116386,
            0.0905767,
            -0.0555024
        ]
    }
}
```

