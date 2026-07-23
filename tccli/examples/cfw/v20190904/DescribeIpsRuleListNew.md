**Example 1: IPS规则查询接口**



Input: 

```
tccli cfw DescribeIpsRuleListNew --cli-unfold-argument  \
    --Filters.0.Name Protocol \
    --Filters.0.Values ANY TCP ICMP \
    --Filters.0.OperatorType 9 \
    --Limit 10 \
    --Offset 0 \
    --Order desc \
    --By sequence
```

Output: 
```
{
    "Response": {
        "ReturnMsg": "xx",
        "ReturnCode": 0,
        "Data": [
            {}
        ],
        "Category": [
            "a",
            "b",
            "c"
        ],
        "RequestId": "xx",
        "Total": 1
    }
}
```

**Example 2: 规则列表最新调用示例**

规则列表最新调用示例

Input: 

```
tccli cfw DescribeIpsRuleListNew --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Category": [
            "SQL注入攻击",
            "web攻击",
            "XSS攻击",
            "一般攻击",
            "信息泄露",
            "已知弱点",
            "恶意文件下载",
            "恶意机器人检测",
            "恶意调用",
            "木马",
            "横向移动",
            "漏洞利用",
            "漏洞利用攻击",
            "网络攻击",
            "网络爆破"
        ],
        "Data": [
            {}
        ],
        "RequestId": "b775e058-734b-4de8-ac54-66f199d5ba88",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 3512
    }
}
```

