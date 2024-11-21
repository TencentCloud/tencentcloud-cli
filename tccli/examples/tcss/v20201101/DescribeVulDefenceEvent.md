**Example 1: 查询漏洞防御事件列表**

DescribeVulDefenceEvent

Input: 

```
tccli tcss DescribeVulDefenceEvent --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CVEID": "CVE-2021-44228",
                "City": "",
                "ClusterID": "",
                "ClusterName": "",
                "ContainerID": "1a00d48467136a768278cbb93fb45b3a7d1cbb7e11ee906eb54cf09bf6a27e5b",
                "ContainerIsolateOperationSrc": "",
                "ContainerName": "/cve-2021-44228-solr-1",
                "ContainerNetStatus": "",
                "ContainerNetSubStatus": "",
                "ContainerStatus": "",
                "CreateTime": "2023-10-08 11:07:16",
                "EventCount": 4,
                "EventID": 20055,
                "EventType": "EVENT_DEFENDED",
                "HostIP": "",
                "HostName": "",
                "ImageID": "sha256:33f2d4bf4fa944682b9c7c1ed66262fe22d488bab7028ce0f676215bade8d92e",
                "ImageName": "vulhub/solr:8.11.0",
                "MergeTime": "2023-10-08 11:07:16",
                "NodeID": "",
                "NodeType": "NORMAL",
                "NodeUniqueID": "",
                "PocID": "pcmgr-333393",
                "PublicIP": "",
                "QUUID": "d9438d70-2689-4013-9ce1-d80edbc29edb",
                "SourceIP": "",
                "Status": "EVENT_DEALED",
                "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
                "PodIP": "1.1.1.1",
                "PodName": "PodName"
            }
        ],
        "TotalCount": 0,
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

