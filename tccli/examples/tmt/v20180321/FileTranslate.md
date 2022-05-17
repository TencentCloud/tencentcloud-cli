**Example 1: 示例1 通过文件数据来调用接口**



Input: 

```
tccli tmt FileTranslate --cli-unfold-argument  \
    --Data eGNmYXNkZmFzZmFzZGZhc2RmCg== \
    --Source zh \
    --Target en \
    --DocumentType pdf \
    --SourceType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Data": {
            "TaskId": 1396665
        }
    }
}
```

