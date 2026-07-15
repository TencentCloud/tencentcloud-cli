**Example 1: 互联网边界防火墙配额展示**



Input: 

```
tccli cfw DescribeSerialRegion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BypassWidth": 386,
        "EdgeElasticBandwidth": 500,
        "EdgeElasticBandwidthLimit": 952,
        "EdgeElasticSwitch": 0,
        "EdgeElasticTrafficSwitch": 1,
        "EdgeWidth": 476,
        "SendBypassWidth": 0,
        "SerialRegionLst": [
            {
                "ElasticBandwidth": 30,
                "ElasticSwitch": 0,
                "ElasticTrafficSwitch": 0,
                "InFlowMax": 65027431,
                "OutFlowMax": 54982426,
                "Region": "ap-chengdu",
                "Width": 30
            }
        ],
        "UnUsedQuota": 12,
        "UnUsedWidth": 0,
        "RequestId": "61306356-34dc-44e6-8a7a-0c5a4aa2727e"
    }
}
```

