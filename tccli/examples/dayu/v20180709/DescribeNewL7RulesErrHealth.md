**Example 1: 获取L7转发规则健康检查异常结果**



Input: 

```
tccli dayu DescribeNewL7RulesErrHealth --cli-unfold-argument  \
    --Business bgpip
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "ErrHealths": [
            {
                "Key": "rule-00000001",
                "Value": "1.1.1.1 400,2.2.2.2 500"
            }
        ]
    }
}
```

