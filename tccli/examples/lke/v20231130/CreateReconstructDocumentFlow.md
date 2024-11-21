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
        "TaskId": "9e28e561e9a04ef096768d13deffe963"
    }
}
```

