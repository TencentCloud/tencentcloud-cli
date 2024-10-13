**Example 1: 示例**

获取用户配额信息

Input: 

```
tccli dsgc GetUserQuotaInfo --cli-unfold-argument  \
    --DspaId abc
```

Output: 
```
{
    "Response": {
        "DspaId": "abc",
        "DbTotalQuota": 0,
        "CosTotalQuota": 0,
        "DbRemainQuota": 0,
        "CosRemainQuota": 0,
        "CosQuotaUnit": "abc",
        "DBUnbindNum": 0,
        "COSUnbindNum": 0,
        "InsTotalQuota": 0,
        "InsRemainQuota": 0,
        "Version": "abc",
        "RequestId": "abc"
    }
}
```

