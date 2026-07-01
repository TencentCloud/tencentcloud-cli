**Example 1: 调整生图任务配额**

设置生图任务配额为1000张图片

Input: 

```
tccli vod CreateAigcQuota --cli-unfold-argument  \
    --SubAppId 200000004 \
    --QuotaType Image \
    --QuotaLimit 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "6eccbd58-caee-4480-8048-90bff384404c"
    }
}
```

