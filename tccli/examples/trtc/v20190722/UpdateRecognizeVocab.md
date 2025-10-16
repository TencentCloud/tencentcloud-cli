**Example 1: 更新热词表**

用户通过该API传入已经创建的热词表ID，可以更新其相应的内容

Input: 

```
tccli trtc UpdateRecognizeVocab --cli-unfold-argument  \
    --VocabId e88178ea56d94397a9acd6a82ec212ce \
    --WordWeights.0.Word test \
    --WordWeights.0.Weight 3
```

Output: 
```
{
    "Response": {
        "RequestId": "61644a68-cd77-472b-9fe6-ad763a9ac8e0",
        "VocabId": "e88178ea56d94397a9acd6a82ec212ce"
    }
}
```

