**Example 1: 示例**

获取用户配额信息

Input: 

```
tccli dsgc GetUserQuotaInfo --cli-unfold-argument  \
    --DspaId dspa-12cd45g7
```

Output: 
```
{
    "Response": {
        "DspaId": "dspa-12cd45g7",
        "DbTotalQuota": 0,
        "CosTotalQuota": 0,
        "DbRemainQuota": 0,
        "CosRemainQuota": 0,
        "CosQuotaUnit": "TB",
        "DBUnbindNum": 0,
        "COSUnbindNum": 0,
        "InsTotalQuota": 0,
        "InsRemainQuota": 0,
        "Version": "standard",
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

