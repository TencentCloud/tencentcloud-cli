**Example 1: 查询每个地域可创建的 ALB 实例数**



Input: 

```
tccli alb DescribeQuota --cli-unfold-argument  \
    --QuotaTypes alb_quota_loadbalancers_num
```

Output: 
```
{
    "Response": {
        "Quotas": [
            {
                "Available": null,
                "Limit": 60,
                "QuotaType": "alb_quota_loadbalancers_num",
                "ResourceId": "alblcu-e8p3x9mq",
                "Used": null
            }
        ],
        "RequestId": "c6585b63-353a-48cb-93ec-b23321e3b7ea"
    }
}
```

