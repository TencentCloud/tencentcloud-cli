**Example 1: 查询标签策略已绑定的对象**

查询标签策略已绑定的对象

Input: 

```
tccli tag ListTargetsForPolicy --cli-unfold-argument  \
    --Limit 20 \
    --PolicyId 10004 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Targets": [
            {
                "TargetId": 100000548134
            }
        ],
        "RequestId": "8c2d5819-320a-4193-99ce-f52999fae113"
    }
}
```

