**Example 1: 获取指定分类和状态的漏洞列表**

获取指定分类和状态的漏洞列表数据

Input: 

```
tccli cwp DescribeVulList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "VulInfoList": [
            {
                "Ids": "1",
                "Name": "Apache Log4j 1.x JNDI 注入漏洞（CVE-2021-4104）",
                "VulId": 34338,
                "Status": 0,
                "PublishTime": "2021-12-14 20:15:00",
                "LastTime": "2024-10-21 17:20:13",
                "HostCount": 1,
                "Level": 3,
                "From": 0,
                "Descript": "Apache Log4j是美国阿帕奇（Apache）基金会的一款基于Java的开源日志记录工具。 \nApache Log4j 1.2存在代码问题漏洞，攻击者可利用该漏洞通过JMSApender反序列化来运行代码。",
                "PublishTimeWisteria": "",
                "NameWisteria": "",
                "DescriptWisteria": "",
                "CveId": "CVE-2021-4104",
                "CvssScore": 7.5,
                "Labels": "远程利用,存在POC",
                "IsSupportDefense": 0,
                "FixSwitch": 1,
                "TaskId": 1,
                "StatusStr": "",
                "DefenseAttackCount": 0,
                "FirstAppearTime": "2024-10-18T01:22:06+08:00",
                "VulCategory": 4,
                "AttackLevel": 0,
                "FixNoNeedRestart": false,
                "Method": 0,
                "VulFixSwitch": 1
            }
        ],
        "TotalCount": 1,
        "FollowVulCount": 1,
        "RequestId": "abc"
    }
}
```

