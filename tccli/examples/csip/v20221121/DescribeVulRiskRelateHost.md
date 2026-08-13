**Example 1: 获取漏洞关联主机**

获取漏洞关联主机

Input: 

```
tccli csip DescribeVulRiskRelateHost --cli-unfold-argument  \
    --KBID 0 \
    --VulID 45230 \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Limit 10 \
    --Offset 0 \
    --Order desc \
    --By LatestScanTime
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Account": {
                    "AppID": 260083796,
                    "Nick": "700002365149",
                    "Uin": "700002365149"
                },
                "AgentStatus": "ONLINE",
                "CloudTag": [],
                "DefendStatus": "NOT_ENABLED",
                "DefendVersion": "BASIC",
                "InstanceID": "ins-f9mhqqxa",
                "InstanceStatus": "RUNNING",
                "Name": "yancyw自建集群",
                "PrivateIP": "172.16.0.2",
                "PublicIP": "",
                "RiskStatus": "PENDING",
                "TagItem": [],
                "VPRRating": {
                    "Remark": "",
                    "Result": "",
                    "Stage": []
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "c5752296-cc49-4e64-bba5-62c19174239c"
    }
}
```

