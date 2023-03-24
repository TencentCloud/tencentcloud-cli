**Example 1: 修改片头片尾模板**

修改片头片尾模板。

Input: 

```
tccli vod ModifyHeadTailTemplate --cli-unfold-argument  \
    --Definition 10000 \
    --Name 模板1 \
    --HeadCandidateSet 1234422xxxx123 \
    --TailCandidateSet 1234422xxxx124
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-xxxx-9d4b-5594145287e1"
    }
}
```

