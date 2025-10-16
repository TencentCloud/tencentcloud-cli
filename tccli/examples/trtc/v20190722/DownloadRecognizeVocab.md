**Example 1: 下载热词表**

用户通过该接口可以获得相应热词表里的内容， 即 word|weight 形式的 base64 值。

Input: 

```
tccli trtc DownloadRecognizeVocab --cli-unfold-argument  \
    --VocabId a6c66d9721b840219674660c32755599
```

Output: 
```
{
    "Response": {
        "RequestId": "584f361d-004e-4781-a3d6-ce6aa9713bcf",
        "VocabId": "a6c66d9721b840219674660c32755599",
        "WordWeightStr": "5rWL6K+V5Yib5bu6NXwzCua1i+ivleWIm+W7ujZ8Nw=="
    }
}
```

