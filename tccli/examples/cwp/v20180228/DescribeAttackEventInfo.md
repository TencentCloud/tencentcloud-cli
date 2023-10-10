**Example 1: 网络攻击事件详情**

网络攻击事件详情

Input: 

```
tccli cwp DescribeAttackEventInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "NetAttackEventInfo": {
            "AbnormalAction": "",
            "AttackLevel": 3,
            "CVEId": "CVE-2021-44228",
            "Count": 5,
            "DstPort": 8080,
            "HostOpType": 0,
            "Id": 1,
            "Location": "局域网",
            "MergeTime": "2023-05-27 14:37:51",
            "NetPayload": "",
            "PayVersion": 0,
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "SrcIP": "10.0.0.5",
            "Status": 1,
            "SvcPs": "eyJhY2NvdW50IjoiMDowIiwiYXJndiI6Im5naW54OiBtYXN0ZXIgcHJvY2VzcyAuL3NiaW4vbmdpbnggLWMgY29uZi95dW5qaW5nLXByb3h5LWRldi5jb25mIC1wIC91c3IvbG9jYWwvc2VydmljZS95dW5qaW5nLXByb3h5IiwiZXhlIjoiL3Vzci9sb2NhbC9zZXJ2aWNlL3l1bmppbmctcHJveHkvc2Jpbi9uZ2lueCIsImxpc3RlbiI6IjAuMC4wLjA6ODA4MHwwLjAuMC4wOjkwODB8MC4wLjAuMDo1NTc0fDAuMC4wLjA6ODAiLCJwaWQiOjMyMzg1Mjh9",
            "Type": 0,
            "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "VulDefenceStatus": 0,
            "VulId": 101824,
            "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
            "VulSupportDefense": 1
        },
        "RequestId": "c9669e5d-8093-4142-b4db-d03e15239235"
    }
}
```

