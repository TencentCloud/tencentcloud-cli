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
        "TotalCount": 0,
        "List": [
            {
                "HostID": "xx",
                "HostName": "xx",
                "ContainerID": "xx",
                "PublicIP": "xx",
                "PodIP": "xx",
                "PodName": "xx",
                "ContainerName": "xx",
                "HostIP": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

