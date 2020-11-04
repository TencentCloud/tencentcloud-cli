**Example 1: 查询配额**



Input: 

```
tccli clb DescribeQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "TOTAL_OPEN_CLB_QUOTA",
                "QuotaLimit": 50,
                "QuotaCurrent": 2
            },
            {
                "QuotaId": "TOTAL_INTERNAL_CLB_QUOTA",
                "QuotaLimit": 100,
                "QuotaCurrent": 3
            },
            {
                "QuotaId": "TOTAL_LISTENER_QUOTA",
                "QuotaLimit": 50,
                "QuotaCurrent": null
            },
            {
                "QuotaId": "TOTAL_TARGET_BIND_QUOTA",
                "QuotaLimit": 50,
                "QuotaCurrent": null
            },
            {
                "QuotaId": "TOTAL_LISTENER_RULE_QUOTA",
                "QuotaLimit": 50,
                "QuotaCurrent": null
            }
        ],
        "RequestId": "92e23338-bccb-4950-8b0d-b3d50e05975b"
    }
}
```

