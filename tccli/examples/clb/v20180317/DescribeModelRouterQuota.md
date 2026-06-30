**Example 1: 查询配额**



Input: 

```
tccli clb DescribeModelRouterQuota --cli-unfold-argument  \
    --QuotaTypes cmr_quota_enterprise_model_router_num \
    --ResourceIds cmr-oei1qdkf \
    --DisplayFields Available
```

Output: 
```
{
    "Response": {
        "Quotas": [
            {
                "Available": 100,
                "Limit": 100,
                "QuotaType": "cmr_quota_enterprise_model_router_num",
                "ResourceId": "cmr-oei1qdkf",
                "Used": null
            }
        ],
        "RequestId": "d4ad5923-a10d-4e0d-8b75-b76e472ecddd"
    }
}
```

