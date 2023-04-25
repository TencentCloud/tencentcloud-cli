**Example 1: 文件翻译结果查询调用示例**

通过文件数据来调用接口

Input: 

```
tccli tmt GetFileTranslate --cli-unfold-argument  \
    --TaskId 100001
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": "Wait",
            "FileData": "",
            "TaskId": "100001",
            "Message": "",
            "Progress": 80
        },
        "RequestId": "1e1cffb3-3637-47f3-b6ef-5b529e08c3c8"
    }
}
```

