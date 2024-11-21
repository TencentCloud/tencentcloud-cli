**Example 1: 查询web应用漏洞列表**



Input: 

```
tccli tcss DescribeWebVulList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CVEID": "CVE-2022-23302",
                "CVSSV3Score": 8.8,
                "Category": "DESERIALIZATION_OF_UNTRUSTED_DATA",
                "ContainerCount": 0,
                "DefenceHostCount": 0,
                "DefenceScope": "",
                "DefenceStatus": "",
                "DefendedCount": 0,
                "FoundTime": "2024-10-29 11:56:21",
                "ID": 173840040,
                "LatestFoundTime": "2024-10-29 11:56:21",
                "Level": "HIGH",
                "LocalImageCount": 0,
                "Name": "Apache log4j JMSSink反序列化代码执行漏洞（CVE-2022-23302）",
                "PocID": "pcmgr-335818",
                "RegistryImageCount": 1,
                "Tags": [
                    "NETWORK",
                    "POC"
                ]
            }
        ],
        "RequestId": "e8f59b70-321a-423d-9f8a-a587451c19dd",
        "TotalCount": 33
    }
}
```

