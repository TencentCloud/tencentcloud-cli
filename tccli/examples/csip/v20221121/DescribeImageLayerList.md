**Example 1: 查询镜像层信息列表**



Input: 

```
tccli csip DescribeImageLayerList --cli-unfold-argument  \
    --Id 802 \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "LayerList": [
            {
                "CriticalLevelVulCnt": 0,
                "HighLevelVulCnt": 0,
                "LayerCmd": "ADD alpine-minirootfs-3.23.3-x86_64.tar.gz / # buildkit",
                "LayerId": "sha256:589002ba0eaed121a1dbf42f6648f29e5be55d5c8a6ee0f8eaa0285cc21ac153",
                "LayerIndex": 0,
                "LowLevelVulCnt": 0,
                "MediumLevelVulCnt": 0,
                "SensitiveCnt": 0,
                "Size": 3861821,
                "VirusCnt": 0
            }
        ],
        "TotalCount": 11,
        "RequestId": "daf3db40-d4ba-41bc-b910-efb7cd4bb444"
    }
}
```

