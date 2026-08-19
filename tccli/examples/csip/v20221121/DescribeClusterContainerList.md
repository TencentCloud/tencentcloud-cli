**Example 1: 调用示例**



Input: 

```
tccli csip DescribeClusterContainerList --cli-unfold-argument  \
    --ClusterAssetId 86693c5bf9e9fbdce993d557b1038fd8 \
    --MemberId mem-a6df317cb6a8c424 \
    --ClusterCaMD5 ddfda8***********************ddc
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppID": 260083796,
                "AssetId": "16b1e3113189bf28db0584ea67dab7ee67d2fe2b170d7b6456d09caf73e49ea4",
                "ContainerId": "16b1e3113189bf28db0584ea67dab7ee67d2fe2b170d7b6456d09caf73e49ea4",
                "ContainerName": "[yunjing-agent-zbldl]yunjing-agent",
                "ImageId": "ccr.ccs.tencentyun.com/yunjing_agent/agent@sha256:c35369e4b827e0054305354be9f74728e87ade34df23deb92dbd9450b098f2c4",
                "ImageName": "ccr.ccs.tencentyun.com/yunjing_agent/agent:latest",
                "NodeId": "",
                "NodeType": "",
                "PodName": "tcss-asset-66c6b4cc44-4v8vl",
                "PodUid": "a08a96938d70342df1a8f0c115277a07",
                "RunStatus": "RUNNING"
            }
        ],
        "TotalCount": 17,
        "RequestId": "6e498acb-a6a0-4d6d-96da-369b2c02bb58"
    }
}
```

