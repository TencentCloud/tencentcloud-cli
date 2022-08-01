**Example 1: 删除7层监听器转发规则**

删除7层监听器转发规则

Input: 

```
tccli gaap DeleteRule --cli-unfold-argument  \
    --Force 1 \
    --ListenerId 0 \
    --RuleId rule-18vhg67
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

