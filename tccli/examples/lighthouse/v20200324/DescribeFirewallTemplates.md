**Example 1: 查询防火墙模板**

查询防火墙模板

Input: 

```
tccli lighthouse DescribeFirewallTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "0ac2ecce-f83b-4f5b-80d2-9e88a07e98c0",
        "TemplateSet": [
            {
                "CreatedTime": "2023-06-20T08:04:09Z",
                "TemplateId": "lhft-6brh0ciy",
                "TemplateName": "test-modify",
                "TemplateState": "NORMAL",
                "TemplateType": "PRIVATE"
            }
        ],
        "TotalCount": 1
    }
}
```

