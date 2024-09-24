**Example 1: ReconstructDocumentSSE处理中回包示例**



Input: 

```
tccli lkeap ReconstructDocumentSSE --cli-unfold-argument  \
    --FileType PDF \
    --FileUrl https://ocr.example.pdf
```

Output: 
```
{
    "RequestId": "0c7bbfbc-641a-4321-bee2-56b1e1e046e9",
    "TaskId": "0c7bbfbc-641a-4321-bee2-56b1e1e046e9",
    "ResponseType": "PROGRESS",
    "Progress": "0",
    "ProgressMessage": "开始文档解析",
    "DocumentRecognizeResultUrl": "",
    "FailedPages": []
}
```

**Example 2: ReconstructDocumentSSE处理完成回包示例**



Input: 

```
tccli lkeap ReconstructDocumentSSE --cli-unfold-argument  \
    --FileType PDF \
    --FileUrl https://ocr.example.pdf
```

Output: 
```
{
    "RequestId": "0c7cabfbc-641a-4321-bee2-56b1e1adwq6e9",
    "TaskId": "0c7bbfbc-641a-4321-bee2-5dds1e1e04fe9",
    "ResponseType": "TASK_RSP",
    "Progress": "100",
    "ProgressMessage": "完成文档解析",
    "DocumentRecognizeResultUrl": "https://document-restruction-sse-1258344699.cos.ap-guangzhou.myqcloud.com/output_files%2F0c7bbfbc-641a-4321-bee2-545de1e046e9_parse.zip?q-sign-algorithm=sha1&q-ak=AKddFap6HLNbidLwPqOrAKGzXrx40scL7l&q-sign-time=1720006266%3B1720006866&q-key-time=1720006266%3B1720006866&q-header-list=host&q-url-param-list=&q-signature=e0e79876549e68f2ae9dbf5df1e516f8f1",
    "FailedPages": []
}
```

