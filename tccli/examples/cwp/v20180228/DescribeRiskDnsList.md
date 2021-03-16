**Example 1: 获取恶意请求列表**

入侵检测-获取恶意请求列表

Input: 

```
tccli cwp DescribeRiskDnsList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

