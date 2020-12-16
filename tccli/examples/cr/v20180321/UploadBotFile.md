**Example 1: 上传机器人文件**



Input: 

```
tccli cr UploadBotFile --cli-unfold-argument  \
    --Module AiApi \
    --Operation Upload \
    --FileType input \
    --FileUrl https://www.qq.com/a.xlsx \
    --FileName abc.xlsx \
    --BotName qtest01
```

Output: 
```
{
    "Response": {
        "RequestId": "12345-6789-test-from-rest4api"
    }
}
```

