**Example 1: 接口请求成功示例**



Input: 

```
tccli lke CreateReconstructDocumentFlow --cli-unfold-argument  \
    --FileStartPageNumber 1 \
    --FileEndPageNumber 1 \
    --Config.TableResultType 1 \
    --FileBase64 data:application/pdf;base64,JVBERi0xLjcKXXX...
```

Output: 
```
{
    "Response": {
        "RequestId": "1d569fb4-4c9d-4141-bbd7-e1d8735bd1a9",
        "TaskId": "63d30100c7534a82a7eaea10d2ae48a2"
    }
}
```

