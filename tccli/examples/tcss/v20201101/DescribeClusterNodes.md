**Example 1: 查询集群节点信息**

查询集群节点信息

Input: 

```
tccli tcss DescribeClusterNodes --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ClusterId cls-abhq0j4o
```

Output: 
```
{
    "Response": {
        "ClusterNodeList": [
            {
                "AgentStatus": "ONLINE",
                "ChargeCoresCnt": 0,
                "DefendStatus": "UnDefended",
                "HostID": "d4cfa6cc-a6a5-49da-a050-cb5892f60e3f",
                "InstanceId": "ins-qj24hgj0",
                "InstanceRole": "MASTER",
                "InstanceState": "Running",
                "MachineType": "CVM",
                "NodeName": "tke_cls-abhq0j4o_master_etcd1",
                "NodeType": "NORMAL",
                "PrivateIpAddresses": "10.0.0.14",
                "PublicIP": "119.29.217.177",
                "UUID": "d4cfa6cc-a6a5-49da-a050-cb5892f60e3f"
            }
        ],
        "RequestId": "c803edab-2a2d-4274-917c-8dd0a806e53d",
        "TotalCount": 4
    }
}
```

