**Example 1: 查询1分钱抵扣详情**

查询1分钱抵扣详情

Input: 

```
tccli tcb DescribeSpecialCostItems --cli-unfold-argument  \
    --EnvId cdnheader-v2a \
    --StartTime 2021-09-09 \
    --EndTime 2021-09-09
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351",
        "SpecialCostItems": [
            {
                "EnvId": "lbvliu-5gfy5n4a0776401d",
                "ReportDate": "2021-07-08",
                "Status": "reported",
                "Uin": "100008561789"
            }
        ]
    }
}
```

