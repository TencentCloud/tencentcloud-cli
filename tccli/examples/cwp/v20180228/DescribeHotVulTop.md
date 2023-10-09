**Example 1: 获取全网热点漏洞**

获取全网热点漏洞

Input: 

```
tccli cwp DescribeHotVulTop --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttackLevel": 3,
                "CveId": "CVE-2023-23638",
                "FixSwitch": 0,
                "Level": 4,
                "Method": 0,
                "Name": "Apache Dubbo 反序列化远程代码执行漏洞（CVE-2023-23638）",
                "PublishDate": "2023-03-08 00:00:00",
                "SupportDefense": 1,
                "VulCategory": 2,
                "VulId": 102561
            },
            {
                "AttackLevel": 3,
                "CveId": "CVE-2023-25194",
                "FixSwitch": 0,
                "Level": 3,
                "Method": 0,
                "Name": "Apache Kafka Connect 远程代码执行漏洞(CVE-2023-25194)",
                "PublishDate": "2023-02-08 00:00:00",
                "SupportDefense": 1,
                "VulCategory": 2,
                "VulId": 102518
            },
            {
                "AttackLevel": 3,
                "CveId": "CVE-2022-42889",
                "FixSwitch": 0,
                "Level": 4,
                "Method": 0,
                "Name": "Apache Commons Text StringLookup 远程代码执行漏洞（CVE-2022-42889）",
                "PublishDate": "2022-10-13 00:00:00",
                "SupportDefense": 1,
                "VulCategory": 2,
                "VulId": 102228
            },
            {
                "AttackLevel": 3,
                "CveId": "CVE-2022-42003",
                "FixSwitch": 0,
                "Level": 3,
                "Method": 0,
                "Name": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42003）",
                "PublishDate": "2022-10-02 00:00:00",
                "SupportDefense": 1,
                "VulCategory": 2,
                "VulId": 102256
            },
            {
                "AttackLevel": 3,
                "CveId": "CVE-2022-33891",
                "FixSwitch": 0,
                "Level": 3,
                "Method": 0,
                "Name": "Apache Spark UI 命令注入漏洞（CVE-2022-33891）",
                "PublishDate": "2022-07-18 00:00:00",
                "SupportDefense": 1,
                "VulCategory": 2,
                "VulId": 102133
            }
        ],
        "RequestId": "0d4c94aa-14b0-4b42-aeec-eeeae3266bb1"
    }
}
```

