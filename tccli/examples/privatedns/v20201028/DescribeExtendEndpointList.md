**Example 1: 查询出站终端节点列表**



Input: 

```
tccli privatedns DescribeExtendEndpointList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "OutboundEndpointSet": [
            {
                "EndpointId": "eid-c8acd39e68d6",
                "EndpointName": "huyue1",
                "EndpointServiceSet": [
                    {}
                ],
                "ForwardLinkArch": "V2R",
                "Region": "ap-guangzhou",
                "Tags": []
            }
        ],
        "TotalCount": 25,
        "RequestId": "279903da-3f6a-44cb-9c31-cad8d018b198"
    }
}
```

