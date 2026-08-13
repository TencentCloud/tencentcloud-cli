**Example 1: 获取组件关联的主机**

获取组件关联的主机

Input: 

```
tccli csip DescribeVulComponentRelateHost --cli-unfold-argument  \
    --VulID 45230 \
    --Name socat \
    --MemberId mem-*******-6f5795752f66e429 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "EffectVersion": "1.7.3.2-2.el7",
                "FixCommand": "sudo yum update socat\n",
                "HostInfo": {
                    "Account": {
                        "AppID": 260000006,
                        "Nick": "700002365149",
                        "Uin": "700002365149"
                    },
                    "AgentStatus": "ONLINE",
                    "CloudTag": [],
                    "InstanceID": "ins-f9mhqqxa",
                    "InstanceStatus": "RUNNING",
                    "Name": "yancyw自建集群",
                    "PrivateIP": "172.16.0.2",
                    "PublicIP": "",
                    "QUUID": "21fb6c0b-3d49-4529-bd32-7739ab4d9d7c",
                    "TagItem": [],
                    "UUID": "21fb6c0b-3d49-4529-bd32-7739ab4d9d7c"
                },
                "Name": "socat",
                "Path": "/usr/bin/socat",
                "ProcessID": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "655d8573-eadb-4ae6-8629-77dbf1da1006"
    }
}
```

