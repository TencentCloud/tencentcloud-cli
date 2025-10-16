**Example 1: 设置热词表状态**

用户通过该接口可以将热词表设置为默认状态（State=1），或者取消默认状态（State=0）。

Input: 

```
tccli trtc SetVocabState --cli-unfold-argument  \
    --VocabId 2f3970e3515b4acaa26eaff759e223e8 \
    --State 0
```

Output: 
```
{
    "Response": {
        "RequestId": "23a7370e-d38f-4451-8940-b5dd6021f8cd",
        "VocabId": "2f3970e3515b4acaa26eaff759e223e8"
    }
}
```

