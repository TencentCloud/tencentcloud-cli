**Example 1: 查询漏洞防御白名单**

查询漏洞防御白名单

Input: 

```
tccli cwp DescribeRaspRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CreateTime": "2024-10-17 17:32:13",
                "CveID": "CVE-2012-4453",
                "Id": 2,
                "ModifyTime": "2024-10-17 17:32:13",
                "Status": 0,
                "SupportDefense": 2,
                "URLRegexp": "",
                "VulVulsID": 1,
                "VulVulsName": "dracut 权限许可和访问控制漏洞 (CVE-2012-4453)",
                "WhiteType": 1
            },
            {
                "CreateTime": "2024-10-17 17:32:13",
                "CveID": "CVE-2016-5003",
                "Id": 3,
                "ModifyTime": "2024-10-17 17:32:13",
                "Status": 0,
                "SupportDefense": 1,
                "URLRegexp": "",
                "VulVulsID": 18878,
                "VulVulsName": "Apache Archiva Apache XML-RPC库安全漏洞(CVE-2016-5003)",
                "WhiteType": 1
            },
            {
                "CreateTime": "2024-10-17 17:28:05",
                "CveID": "CVE-2012-4453",
                "Id": 1,
                "ModifyTime": "2024-10-17 17:28:05",
                "Status": 0,
                "SupportDefense": 2,
                "URLRegexp": "regexp",
                "VulVulsID": 1,
                "VulVulsName": "dracut 权限许可和访问控制漏洞 (CVE-2012-4453)",
                "WhiteType": 0
            }
        ],
        "RequestId": "2214a590-b84b-4a97-acdd-8de9331ccfc9",
        "TotalCount": 3
    }
}
```

