**Example 1: 创建片头片尾模板**

创建片头片尾模板。

Input: 

```
tccli vod CreateHeadTailTemplate --cli-unfold-argument  \
    --Name 模板名 \
    --Comment 模板描述 \
    --HeadCandidateSet 1234422xxxx123 \
    --TailCandidateSet 1234422xxxx124
```

Output: 
```
{
    "Response": {
        "Definition": 1000,
        "RequestId": "12ae8d8e-xxxx-9d4b-5594145287e1"
    }
}
```

