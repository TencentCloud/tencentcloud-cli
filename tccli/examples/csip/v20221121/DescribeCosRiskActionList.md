**Example 1: 风险接口列表信息**



Input: 

```
tccli csip DescribeCosRiskActionList --cli-unfold-argument  \
    --RelAppId 1372183813 \
    --BucketName brain-13712132323 \
    --PolicyId 34
```

Output: 
```
{
    "Response": {
        "RequestId": "req-123456789",
        "Data": [
            {
                "ActionName": "GetObject",
                "ActionNameCn": "获取对象",
                "ActionAccessTime": 172814214,
                "InvokeCount": 1250
            }
        ],
        "Total": 10
    }
}
```

