**Example 1: 查询漏洞防御的主机列表**

查询漏洞防御的主机列表

Input: 

```
tccli tcss DescribeVulDefenceHost --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "CreateTime": "2023-08-17 15:41:32",
                "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
                "HostIP": "1.1.1.1",
                "HostName": "tcs-test",
                "ModifyTime": "2024-10-30 14:00:21",
                "NodeID": "ins-8bc803fd",
                "NodeSubNetCIDR": "10.0.200.0/24",
                "NodeSubNetID": "subnet-5gu2***",
                "NodeSubNetName": "subnet***",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
                "PublicIP": "1.1.1.1",
                "Status": "SUCCESS"
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

