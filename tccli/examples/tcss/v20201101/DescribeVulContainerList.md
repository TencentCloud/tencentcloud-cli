**Example 1: 查询受漏洞的容器列表**



Input: 

```
tccli tcss DescribeVulContainerList --cli-unfold-argument  \
    --PocID 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ClusterID": "68b68a372df3394bf46f7320707ebdcd",
                "ClusterName": "default-cluster",
                "ContainerID": "0b70affcd1c495798c2fbde915a43e94df0457c204848be862ad0689aab868a6",
                "ContainerName": "containner",
                "HostID": "5c442550-bbbc-aaaa-ada3-00796bd9fefe",
                "HostIP": "10.206.64.13",
                "HostName": "tcs-sssa",
                "NodeID": "",
                "NodeName": "",
                "NodeType": "NORMAL",
                "NodeUniqueID": "",
                "PodIP": "",
                "PodName": "",
                "PublicIP": "1.2.3.4"
            }
        ],
        "RequestId": "e33b04ca-8e2f-4242-946f-2804debc5c9b",
        "TotalCount": 31
    }
}
```

