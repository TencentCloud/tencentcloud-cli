**Example 1: 创建自动化告警规则**

创建自动化告警规则

Input: 

```
tccli hasim CreateRule --cli-unfold-argument  \
    --Name demo \
    --Type 101 \
    --IsActive True \
    --Notice 1 \
    --Email xxx@xx.com
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

