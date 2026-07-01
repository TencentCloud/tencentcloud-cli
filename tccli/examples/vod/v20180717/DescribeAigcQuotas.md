**Example 1: 查询生图任务配额**



Input: 

```
tccli vod DescribeAigcQuotas --cli-unfold-argument  \
    --SubAppId 251382264 \
    --QuotaType Image
```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaLimit": 2000,
                "QuotaType": "Image",
                "Usage": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "f25627b7-fd15-4f51-a90f-7ed4abdf1b72"
    }
}
```

