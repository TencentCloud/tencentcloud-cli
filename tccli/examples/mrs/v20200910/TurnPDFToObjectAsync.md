**Example 1: 体检报告PDF文件结构化异步接口**



Input: 

```
tccli mrs TurnPDFToObjectAsync --cli-unfold-argument  \
    --PdfInfo.Base64 PDF文件转base64之后的信息
```

Output: 
```
{
    "Response": {
        "TaskID": "taskID",
        "RequestId": "1cf14582-bd61-4ea2-93ca-c63eaa8d427a"
    }
}
```

