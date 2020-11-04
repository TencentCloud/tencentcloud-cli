**Example 1: 查询黑石EIP 限额**



Input: 

```
tccli bmeip DescribeEipQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EipNumQuota": 100,
        "CurrentEipNum": 14,
        "DailyApplyCount": 70,
        "DailyApplyQuota": 200,
        "BatchApplyMax": 20,
        "RequestId": "1eefd65f-264f-4997-8a7b-115a08be2aec"
    }
}
```

