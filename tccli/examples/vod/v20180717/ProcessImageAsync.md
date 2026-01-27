**Example 1: 发起图片异步处理**



Input: 

```
tccli vod ProcessImageAsync --cli-unfold-argument  \
    --SubAppId 221073 \
    --FileId 966263618924724112 \
    --ImageTaskInput.Definition 7
```

Output: 
```
{
    "Response": {
        "TaskId": "221073-ProcessImageAsync-aada17cb6859b9051afe22383fa596d7t",
        "RequestId": "4b91e385-e5b1-4e46-9172-f9188c560ef9"
    }
}
```

