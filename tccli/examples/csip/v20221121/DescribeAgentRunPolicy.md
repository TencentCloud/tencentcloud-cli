**Example 1: 查询**



Input: 

```
tccli csip DescribeAgentRunPolicy --cli-unfold-argument  \
    --MemberId mem-tencent-54213b157ddf7170
```

Output: 
```
{
    "Response": {
        "AdvanceModeInstanceIDs": [
            "ins-0votwsua"
        ],
        "AdvancePolicy": {
            "Cpu": 30,
            "Memory": 0,
            "NetworkPps": 100000
        },
        "BasicPolicy": {
            "Cpu": 10,
            "Memory": 0,
            "NetworkPps": 30000
        },
        "CustomModeInstanceIDs": [],
        "CustomPolicy": {
            "Cpu": 30,
            "Memory": 0,
            "NetworkPps": 100000
        },
        "RequestId": "0913b989-bf43-40e5-a36e-6cea2c4b58a8"
    }
}
```

