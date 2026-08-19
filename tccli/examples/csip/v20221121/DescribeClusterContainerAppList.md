**Example 1: 1**



Input: 

```
tccli csip DescribeClusterContainerAppList --cli-unfold-argument  \
    --ContainerId c95d6114*********************c20**************************f07968
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ConfigPath": "",
                "ExePath": "/usr/local/bin/node",
                "MainType": "",
                "ProcessCnt": 0,
                "RunAs": "node:node",
                "Type": "node",
                "Version": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "cc349571-3847-45f5-8e02-105a15a64c56"
    }
}
```

