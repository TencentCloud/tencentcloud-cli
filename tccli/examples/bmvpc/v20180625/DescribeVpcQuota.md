**Example 1: DescribeVpcQuota**



Input: 

```
tccli bmvpc DescribeVpcQuota --cli-unfold-argument  \
    --TypeIds 0
```

Output: 
```
{
    "Response": {
        "VpcQuotaSet": [
            {
                "TypeId": 0,
                "Quota": 5
            }
        ],
        "RequestId": "5866860f-4d88-46c5-80ca-683b8ea1e453"
    }
}
```

