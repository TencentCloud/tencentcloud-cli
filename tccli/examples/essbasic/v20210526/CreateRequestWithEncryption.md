**Example 1: 通过加密请求体进行请求**



Input: 

```
tccli essbasic CreateRequestWithEncryption --cli-unfold-argument  \
    --RequestAction DescribeFlowComponents \
    --ApplicationId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --IV mJc2aKe4B71d9p62y6bp2A== \
    --EncryptedData riUP2CKf+QGCfN9VMjTgCbsPidmXJulBUD8jxdg3YZwecWCF1CTg+4zB1nEICbGPRedPjF0+zZ1ybTDEc/xG/nQ5J7n4+uNiWCCOqRsjDcwzoD1gZ+y1W++qdjjCns/z8SMxciKmSS7h/cL5kwUARg== \
    --EncryptionSignature vzOw7yV+oAaYBmpbDDGfl7OGxuN3M38IjpJG/mTnEzE=
```

Output: 
```
{
    "Response": {
        "EncryptedData": "a5iZ2f7i02NJZQ4ErVIxbJffDsp/7mdTX1KcS3SGmWmy6B0MhdJx8sWFsP10RJjgiXyBxBDlPI3GMnFMrXLTgv+FMsNjSegEJwJCHsPQ5fzRkhuA9084LviPMFQuKRIDzGHMnHHCR0PerppIupGlEHXga/Cmn5Tx1YZIGESVf8zPncDGttYB8W8HHLVq4Jcg5s2GdjAW95Vu/vt+crXZBFvppLcYB7hja6xZIwkROkE=",
        "EncryptionSignature": "INxBHAiknWJ2tshbEhOGDKjezZMEfhyq6LpSGir4t9s=",
        "IV": "E3j3s8oySTLGgWP25IgRZA==",
        "RequestId": "1dc99e1d-71f1-4841-a5df-d1cb389d018d"
    }
}
```

