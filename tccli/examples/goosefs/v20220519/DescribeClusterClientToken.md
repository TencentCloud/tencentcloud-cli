**Example 1: 查询GooseFS集群客户端凭证**



Input: 

```
tccli goosefs DescribeClusterClientToken --cli-unfold-argument  \
    --ClusterId g_cvm_0yz04uv3
```

Output: 
```
{
    "Response": {
        "ClientTokens": [
            {
                "NodeIp": "127.0.0.1",
                "LocalDirectory": "/data",
                "GooseFSDirectory": "/goosefs",
                "Token": "MTY4ODQ2NTA1NF84MzM2X2E3ZWFmMDVmLWI0MzMtNGE2Yi1iOWU2LTZiZDY5OTYwNThiZQ=="
            }
        ],
        "RequestId": "9ecdc30f-4e06-4995-89b6-ffaf3a085a2e"
    }
}
```

