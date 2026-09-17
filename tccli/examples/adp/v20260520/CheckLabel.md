**Example 1: 校验标签**

校验标签

Input: 

```
tccli adp CheckLabel --cli-unfold-argument  \
    --KbId 2067622575842400832 \
    --TermList 2067622575842400832
```

Output: 
```
{
    "Response": {
        "CheckList": [
            {
                "CheckResult": {
                    "Passed": false,
                    "Reason": "标准词已存在"
                },
                "Term": "价格",
                "TermId": "1"
            }
        ],
        "RequestId": "de76301d-5863-4a5e-a879-7dbddcc987c0"
    }
}
```

