**Example 1: 创建热词表**

用户通过上传词权重数组方式创建热词表

Input: 

```
tccli asr CreateAsrVocab --cli-unfold-argument  \
    --Name 词表名称 \
    --Description 词表描述 \
    --WordWeights.0.Word 智聆 \
    --WordWeights.0.Weight 1 \
    --WordWeights.1.Word 滨海大厦 \
    --WordWeights.1.Weight 6 \
    --WordWeights.2.Word 存储桶 \
    --WordWeights.2.Weight 8 \
    --WordWeights.3.Word 核保 \
    --WordWeights.3.Weight 10
```

Output: 
```
{
    "Response": {
        "VocabId": "aa6f402f263f12ea856fc81fbecfd0sd",
        "RequestId": "b3808ad3-d8dd-4b65-96c9-7d6f1f81b6b6"
    }
}
```

