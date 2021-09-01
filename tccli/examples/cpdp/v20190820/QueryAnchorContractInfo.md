**Example 1: QueryAnchorContractInfo**



Input: 

```
tccli cpdp QueryAnchorContractInfo --cli-unfold-argument  \
    --BeginTime 2020-01-01 \
    --EndTime 2020-01-02
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1590064374302",
        "AnchorContractInfoList": [
            {
                "AnchorId": "00001",
                "AgentId": "1",
                "AgentName": "假代理商",
                "IdNo": "10086",
                "AnchorName": "假主播"
            },
            {
                "AnchorId": "00002",
                "AgentId": "y",
                "AgentName": "z",
                "IdNo": "10086",
                "AnchorName": "假主播2"
            }
        ]
    }
}
```

