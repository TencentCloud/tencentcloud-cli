**Example 1: 获取防篡改url**



Input: 

```
tccli waf DescribeAntiFakeRules --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name RuleID \
    --Filters.0.Values 1102111 \
    --Filters.0.ExactMatch True \
    --Order desc \
    --By ts
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "08e8410d-6e80-4d1f-89ff-62669042369d",
        "Total": 0
    }
}
```

