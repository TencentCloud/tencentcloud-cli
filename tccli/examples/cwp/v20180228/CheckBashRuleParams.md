**Example 1: 示例**



Input: 

```
tccli cwp CheckBashRuleParams --cli-unfold-argument  \
    --Rule rm -rf /tmp/tmp\.ERYbwgd8e9 \
    --Name mapleaa \
    --EventId 1098230 \
    --CheckField Name,Rule
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "ErrCode": 2,
        "ErrMsg": "正则表达式与命令内容不匹配"
    }
}
```

