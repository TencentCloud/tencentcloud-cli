**Example 1: 创建热词表**

用户通过上传词权重数组方式创建热词表

Input: 

```
tccli trtc CreateRecognizeVocab --cli-unfold-argument  \
    --Name 创建测试 \
    --WordWeights.0.Word 创建测试 \
    --WordWeights.0.Weight 2
```

Output: 
```
{
    "Response": {
        "RequestId": "53d09013-d356-4455-affd-0e1a149f863f",
        "VocabId": "81fce185dabd450e95bf6a98b741455e"
    }
}
```

