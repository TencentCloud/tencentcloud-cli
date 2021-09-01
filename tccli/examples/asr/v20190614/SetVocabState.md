**Example 1: 设置热词表状态**

用户通过该接口可以将热词表设置为默认状态（State=1），或者取消默认状态（State=0）。

Input: 

```
tccli asr SetVocabState --cli-unfold-argument  \
    --VocabId aa6f402f263f12ea856fc81fbecfd0sd \
    --State 1
```

Output: 
```
{
    "Response": {
        "VocabId": "aa6f402f263f12ea856fc81fbecfd0sd",
        "RequestId": "9910af1f-d479-4cb5-a303-b0a4c1c03137"
    }
}
```

