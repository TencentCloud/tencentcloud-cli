**Example 1: 下载任务录音与文本**



Input: 

```
tccli cr DownloadBotRecord --cli-unfold-argument  \
    --Module AiApi \
    --Operation DownloadRecord \
    --BizDate 2020-12-12
```

Output: 
```
{
    "Response": {
        "RecordCosUrl": "",
        "TextCosUrl": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

