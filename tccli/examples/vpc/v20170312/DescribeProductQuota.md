**Example 1: 查询云联网产品配额信息**

查询云联网产品配额信息

Input: 

```
tccli vpc DescribeProductQuota --cli-unfold-argument  \
    --Product "ccn"
```

Output: 
```
{
    "Response": {
        "TotalCount": 53,
        "ProductQuotaSet": [
            {
                "QuotaId": "1",
                "QuotaName": "每个开发商可创建的CCN对象个数",
                "QuotaCurrent": 50,
                "QuotaLimit": 100,
                "QuotaRegion": false
            },
            {
                "QuotaId": "2",
                "QuotaName": "每个CCN对象可关联的实例个数",
                "QuotaCurrent": 25,
                "QuotaLimit": 1000,
                "QuotaRegion": false
            }
        ],
        "RequestId": "a1dfbcc0-947a-44a4-9257-781e9f1e2ad3"
    }
}
```

