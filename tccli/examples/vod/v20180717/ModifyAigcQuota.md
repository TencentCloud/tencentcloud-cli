**Example 1: 调整生图任务配额**



Input: 

```
tccli vod ModifyAigcQuota --cli-unfold-argument  \
    --SubAppId 200000004 \
    --QuotaType Image \
    --QuotaLimit 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "fd44c32f-5ccc-4bd4-a6cc-f07e006182f7"
    }
}
```

