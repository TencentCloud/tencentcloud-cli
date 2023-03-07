**Example 1: 忽略规则关联的主机**



Input: 

```
tccli cwp DescribeBaselineHostIgnoreList --cli-unfold-argument  \
    --RuleID 126
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostId": "d8feb20e-dcdd-461b-9b37-336c42d48657",
                "HostName": "功能测试软件较多_ivon",
                "HostTag": "",
                "HostIp": "172.16.0.49",
                "WanIp": "10.104.9.1"
            }
        ],
        "RequestId": "0eb82ff4-667a-4525-82b5-e304aee952ee",
        "Total": 1
    }
}
```

