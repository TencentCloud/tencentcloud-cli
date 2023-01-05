**Example 1: 编辑自动化规则**

编辑自动化规则

Input: 

```
tccli hasim ModifyRule --cli-unfold-argument  \
    --Name demo \
    --Type 101 \
    --IsActive True \
    --Notice 1 \
    --Email xxx@xx.com \
    --RuleID 10010
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

