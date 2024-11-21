**Example 1: 获取运行时安全事件新增趋势**



Input: 

```
tccli tcss DescribeImageRiskTendency --cli-unfold-argument  \
    --EndTime 2020-09-22 \
    --StartTime 2020-09-22
```

Output: 
```
{
    "Response": {
        "ImageRiskTendencySet": [
            {
                "ImageRiskSet": [
                    {
                        "Cnt": 1,
                        "CurTime": "2020-09-22"
                    }
                ],
                "ImageRiskType": "IRT_VULNERABILITY"
            }
        ],
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

