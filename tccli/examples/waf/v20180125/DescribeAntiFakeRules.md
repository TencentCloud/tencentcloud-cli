**Example 1: 获取防篡改url**



Input: 

```
tccli waf DescribeAntiFakeRules --cli-unfold-argument  \
    --Domain abc \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --Order abc \
    --By abc
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

