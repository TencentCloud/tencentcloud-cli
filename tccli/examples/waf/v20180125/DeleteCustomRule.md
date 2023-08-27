**Example 1: 删除指定的自定义规则**



Input: 

```
tccli waf DeleteCustomRule --cli-unfold-argument  \
    --Domain www.test.com \
    --Edition clb-waf \
    --RuleId 501
```

Output: 
```
{
    "Response": {
        "RequestId": "26b0ac84-cb08-49d2-9899-4206d1849a41"
    }
}
```

