**Example 1: 举报侵权链接**



Input: 

```
tccli bma CreateCRTort --cli-unfold-argument  \
    --WorkId 123 \
    --TortURL 侵权链接 \
    --TortPlat 侵权平台 \
    --TortTitle 侵权标题
```

Output: 
```
{
    "Response": {
        "WorkId": 1,
        "TortId": 123,
        "TortTitle": "xxx",
        "TortPlat": "xxx",
        "TortURL": "xxx",
        "TortDomain": "侵权域名",
        "TortBodyName": "侵权主体",
        "RequestId": "xxx"
    }
}
```

