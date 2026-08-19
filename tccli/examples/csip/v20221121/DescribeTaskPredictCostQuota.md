**Example 1: 获取扫描预消耗配额**



Input: 

```
tccli csip DescribeTaskPredictCostQuota --cli-unfold-argument  \
    --TaskMode 1 \
    --MemberId mem-12**** \
    --RuleIDs tc_003
```

Output: 
```
{
    "Response": {
        "CostQuota": 0,
        "RequestId": "b0d4476e-dafc-45a2-b331-8e00ef158ec1"
    }
}
```

