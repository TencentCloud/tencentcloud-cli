**Example 1: 查询带宽包配额**

查询带宽包配额。

Input: 

```
tccli vpc DescribeBandwidthPackageQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "TOTAL_BANDWIDTHPKG_QUOTA",
                "QuotaCurrent": 1,
                "QuotaLimit": 20
            }
        ],
        "RequestId": "8882b478-0d3a-4fe2-bae3-ff93865a199c"
    }
}
```

