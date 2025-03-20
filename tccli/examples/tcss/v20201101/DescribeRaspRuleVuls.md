**Example 1: 查询漏洞白名单里的漏洞列表**

查询漏洞白名单里的漏洞列表

Input: 

```
tccli tcss DescribeRaspRuleVuls --cli-unfold-argument  \
    --Filters.0.Name WhiteType \
    --Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CveID": "cveid",
                "SupportDefense": 1,
                "VulVulsID": 9102851,
                "VulVulsName": "Weblogic T3/IIOP 反序列化漏洞"
            },
            {
                "CveID": "cveid",
                "SupportDefense": 1,
                "VulVulsID": 9102413,
                "VulVulsName": "xstream反序列化漏洞系列"
            },
            {
                "CveID": "cveid",
                "SupportDefense": 1,
                "VulVulsID": 9102408,
                "VulVulsName": "Jackson反序列化漏洞"
            },
            {
                "CveID": "pcmgr-9102137",
                "SupportDefense": 1,
                "VulVulsID": 9102137,
                "VulVulsName": "Apache Struts2 远程代码执行漏洞"
            },
            {
                "CveID": "",
                "SupportDefense": 1,
                "VulVulsID": 9102094,
                "VulVulsName": "java反序列化漏洞"
            },
            {
                "CveID": "pcmgr-9102071",
                "SupportDefense": 1,
                "VulVulsID": 9102071,
                "VulVulsName": "Fastjson 反序列化任意代码执行漏洞"
            },
            {
                "CveID": "pcmgr-9100547",
                "SupportDefense": 1,
                "VulVulsID": 9100547,
                "VulVulsName": "Fastjson 远程代码执行漏洞"
            },
            {
                "CveID": "cveid",
                "SupportDefense": 1,
                "VulVulsID": 9100414,
                "VulVulsName": "Fastjson 反序列化远程代码执行漏洞"
            },
            {
                "CveID": "pcmgr-9100399",
                "SupportDefense": 1,
                "VulVulsID": 9100399,
                "VulVulsName": "Fastjson 远程代码执行漏洞"
            },
            {
                "CveID": "cveid",
                "SupportDefense": 1,
                "VulVulsID": 9100388,
                "VulVulsName": "Fastjson 远程代码执行漏洞"
            }
        ],
        "RequestId": "bbeddb8a-f99d-43a1-aadb-c32e148fdb94",
        "TotalCount": 215
    }
}
```

