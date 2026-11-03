**Example 1: 任务失败场景**



Input: 

```
tccli lkeap GetReconstructDocumentResult --cli-unfold-argument  \
    --TaskId 85f2890d1758900375298
```

Output: 
```
{
    "Response": {
        "RequestId": "3824428a-989f-4d57-992c-b507aa12fbf9",
        "Status": "Failed",
        "TaskErrInfo": {}
    }
}
```

**Example 2: 获取解析结果**



Input: 

```
tccli lkeap GetReconstructDocumentResult --cli-unfold-argument  \
    --TaskId a68882281758900286804
```

Output: 
```
{
    "Response": {
        "DocumentRecognizeResultUrl": "https://example.cos.ap-guangzhou.myqcloud.com/public/example/example.zip",
        "RequestId": "ead3347b-7c39-4fb0-98fb-dad02dd122b9",
        "Status": "Success",
        "Usage": {
            "FileSize": 591574,
            "PageNumber": 17,
            "SuccessPageNum": 17,
            "TotalTokens": 21533
        }
    }
}
```

