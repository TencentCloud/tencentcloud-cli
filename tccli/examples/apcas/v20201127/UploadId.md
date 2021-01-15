**Example 1: 画像洞察导入IMEI列表（base64编码）**



Input: 

```
tccli apcas UploadId --cli-unfold-argument  \
    --Type 0 \
    --TaskName Test123 \
    --IdListBase64 MzUxOTUyMDgwODk1MjQzCjg2OTcwNzAzOTE0MzczMAo4Njc5NzkwNDg0MjY5MjUKODY5MjQ3MDM1OTYyMTE0Cjg2MTI0MzA0MTU3MTk2Mw
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "TaskData": {
            "Id": 0
        }
    }
}
```

