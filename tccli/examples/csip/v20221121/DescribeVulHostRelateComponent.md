**Example 1: 查询主机关联组件**

查询主机关联组件

Input: 

```
tccli csip DescribeVulHostRelateComponent --cli-unfold-argument  \
    --VulID 59720 \
    --InstanceID ins-aurb6wi2 \
    --MemberId mem-tencent-6f5795752f66e429
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "EffectVersion": "3.6.8-21.tl2.3",
                "FixCommand": "sudo yum update python3\n",
                "HostInfo": {
                    "Account": {
                        "AppID": 260082268,
                        "Nick": "成员账号",
                        "Uin": "700002332361"
                    },
                    "AgentStatus": "ONLINE",
                    "CloudTag": [],
                    "InstanceID": "ins-aurb6wi2",
                    "InstanceStatus": "RUNNING",
                    "Name": "自动化-TencentOS 2",
                    "PrivateIP": "172.16.0.51",
                    "PublicIP": "",
                    "QUUID": "70fe263a-080e-4801-8954-10bfb437f9f1",
                    "TagItem": [],
                    "UUID": "70fe263a-080e-4801-8954-10bfb437f9f1"
                },
                "Name": "python3",
                "Path": "/usr/bin/python3",
                "ProcessID": ""
            }
        ],
        "RequestId": "ba5e3ee7-c6ec-4b4d-b9ce-a0283463e032"
    }
}
```

