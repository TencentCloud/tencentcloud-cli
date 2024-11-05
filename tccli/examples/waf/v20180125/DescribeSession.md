**Example 1: Waf 会话定义查询接口**



Input: 

```
tccli waf DescribeSession --cli-unfold-argument  \
    --Domain test.com \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "SessionId": 2000003356,
                    "SessionName": "test-session",
                    "Category": "match",
                    "KeyOrStartMat": "PHPSESSID=",
                    "EndMat": ";",
                    "StartOffset": "-1",
                    "EndOffset": "-1",
                    "Source": "cookie",
                    "TsVersion": "1727147589924",
                    "SessionInUsed": false,
                    "RelatedRuleID": []
                }
            ]
        },
        "RequestId": "88d80896-a330-4a7f-a72f-f5175a20ebcc"
    }
}
```

