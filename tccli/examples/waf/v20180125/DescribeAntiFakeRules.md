**Example 1: 获取防篡改url**



Input: 

```
tccli waf DescribeAntiFakeRules --cli-unfold-argument  \
    --Domain xx \
    --Order xx \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --By xx
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "08e8410d-6e80-4d1f-89ff-62669042369d"
    }
}
```

