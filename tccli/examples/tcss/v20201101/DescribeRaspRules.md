**Example 1: 查询漏洞防御白名单**

查询漏洞防御白名单

Input: 

```
tccli tcss DescribeRaspRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CreateTime": "2024-11-19 19:16:26",
                "CveID": "CVE-2024-37032",
                "Id": 463,
                "ModifyTime": "2024-11-19 19:16:26",
                "Status": 0,
                "SupportDefense": 2,
                "URLRegexp": "",
                "VulVulsID": 105333,
                "VulVulsName": "Ollama远程代码执行漏洞(CVE-2024-37032)",
                "WhiteType": 1
            }
        ],
        "RequestId": "43acddb3-20bf-41d2-a5ca-824cae917760",
        "TotalCount": 1
    }
}
```

