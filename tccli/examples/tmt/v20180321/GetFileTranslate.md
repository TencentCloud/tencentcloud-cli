**Example 1: 示例1 通过文件数据来调用接口**



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
            "Progress": "80"
        },
        "RequestId": "xx"
    }
}
```

