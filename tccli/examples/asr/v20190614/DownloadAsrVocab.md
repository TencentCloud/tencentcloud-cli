**Example 1: 下载热词表**

用户通过该接口可以获得相应热词表里的内容， 即 word|weight 形式的 base64 值。

Input: 

```
tccli asr DownloadAsrVocab --cli-unfold-argument  \
    --VocabId aa6f402f263f12ea856fc81fbecfd0sd
```

Output: 
```
{
    "Response": {
        "VocabId": "aa6f402f263f12ea856fc81fbecfd0sd",
        "WordWeightStr": "5a2X56ym5LiyfDQNCg==",
        "RequestId": "1085dec9-df56-4124-8a6d-acb198177923"
    }
}
```

