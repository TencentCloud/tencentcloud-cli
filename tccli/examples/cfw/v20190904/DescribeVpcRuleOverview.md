**Example 1: vpc规则列表概况**



Input: 

```
tccli cfw DescribeVpcRuleOverview --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --EdgeId cfws-1462d1d278
```

Output: 
```
{
    "Response": {
        "StrategyNum": 70,
        "StartRuleNum": 70,
        "RequestId": "cd0e1fdf-157d-438c-9bc8-75925e5d4e20"
    }
}
```

