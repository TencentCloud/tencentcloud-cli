**Example 1: 语音过滤**



Input: 

```
tccli gme VoiceFilter --cli-unfold-argument  \
    --BizId 0 \
    --FileId test_file_id \
    --FileName test_file_name \
    --FileUrl http%3a%2f%2ftest_file_url.com%2ffile
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

