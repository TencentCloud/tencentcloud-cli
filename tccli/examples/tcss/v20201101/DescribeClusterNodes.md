**Example 1: 查询集群节点信息**

查询集群节点信息

Input: 

```
tccli tcss DescribeClusterNodes --cli-unfold-argument  \
    --ClusterId abc \
    --Offset 1 \
    --Limit 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --By abc \
    --Order abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterNodeList": [
            {
                "InstanceId": "abc",
                "PrivateIpAddresses": "abc",
                "InstanceRole": "abc",
                "InstanceState": "abc",
                "NodeName": "abc",
                "AgentStatus": "abc",
                "PublicIP": "abc",
                "HostID": "abc",
                "MachineType": "abc",
                "NodeType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

