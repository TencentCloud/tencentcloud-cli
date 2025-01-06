**Example 1: 接口请求成功示例**



Input: 

```
tccli lkeap CreateReconstructDocumentFlow --cli-unfold-argument  \
    --FileType PDF \
    --FileUrl http://example.com/example.pdf
```

Output: 
```
{
    "Response": {
        "RequestId": "1d569fb4-4c9d-4141-bbd7-e1d8735bd1a9",
        "TaskId": "123123123"
    }
}
```

