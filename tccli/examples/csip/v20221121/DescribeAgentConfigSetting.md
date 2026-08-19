**Example 1: 查询**



Input: 

```
tccli csip DescribeAgentConfigSetting --cli-unfold-argument  \
    --MemberId mem-tencent-b624e485fee5fe29
```

Output: 
```
{
    "Response": {
        "AssetSelectionType": "direct",
        "EnhanceLogMode": 0,
        "ExcludeInstanceIDs": [],
        "InstanceIDs": [
            "ins-q4pf14qs"
        ],
        "LogCollectSettings": [
            "tcp_ingress"
        ],
        "MalwarePocMode": 0,
        "ReportSourcePort": 0,
        "TagIds": [],
        "RequestId": "82adab1d-9b89-4620-97f5-288d69e1bdaa"
    }
}
```

