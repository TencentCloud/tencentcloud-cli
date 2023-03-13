**Example 1: 检测项列表**

检测项列表

Input: 

```
tccli cwp DescribeBaselineItemIgnoreList --cli-unfold-argument  \
    --RuleID 125
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "529a6a2c-91ef-44e3-a822-953846e0e596",
        "Total": 0
    }
}
```

**Example 2: 忽略检测项列表**

忽略检测项列表

Input: 

```
tccli cwp DescribeBaselineItemIgnoreList --cli-unfold-argument  \
    --RuleID 125
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "529a6a2c-91ef-44e3-a822-953846e0e596",
        "Total": 0
    }
}
```

