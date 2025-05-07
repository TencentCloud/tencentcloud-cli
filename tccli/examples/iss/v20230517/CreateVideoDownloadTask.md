**Example 1: 成功**

 

Input: 

```
tccli iss CreateVideoDownloadTask --cli-unfold-argument  \
    --ChannelId *********** \
    --BeginTime 1729288800 \
    --EndTime 1729292400 \
    --Scale 1 \
    --Expire 7 \
    --FileType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadTaskId": "**********"
        },
        "RequestId": "cd92416f-bc75-4d17-91f3-93d7c94d1cf5"
    }
}
```

