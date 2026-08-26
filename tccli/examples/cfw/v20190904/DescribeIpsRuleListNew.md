**Example 1: 规则列表最新调用示例**

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
            {
                "Action": 1,
                "Category": "XSS攻击",
                "Confidence": "高",
                "Cve": "",
                "DefaultAction": 1,
                "EventName": "XSS攻击",
                "EventNameDesc": "这条规则用于防止黑客通过注入生成一\"onunload\"消息的处理函数，攻击可出现于HTTP请求的URL或者HTTP参数中",
                "FwType": 7,
                "Id": 177919,
                "Level": "高危",
                "RuleID": "20001",
                "RuleType": 2,
                "Status": 1,
                "VulTarget": ""
            }
        ],
        "RequestId": "b775e058-734b-4de8-ac54-66f199d5ba88",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 3512
    }
}
```

