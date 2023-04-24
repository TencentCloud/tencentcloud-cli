**Example 1: 文件翻译请求调用示例**

通过文件数据来调用接口

Input: 

```
tccli tmt FileTranslate --cli-unfold-argument  \
    --SourceType 1 \
    --Source zh \
    --Target en \
    --DocumentType txt \
    --Data 5L2g5aW944CC
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Data": {
            "TaskId": "1396665"
        }
    }
}
```

