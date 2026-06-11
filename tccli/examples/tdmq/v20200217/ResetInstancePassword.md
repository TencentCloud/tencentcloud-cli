**Example 1: 创建轮转角色**



Input: 

```
tccli tdmq ResetInstancePassword --cli-unfold-argument  \
    --SecretName dadas \
    --UserResourceId pulsar-op4og4jmozvk \
    --ResourceAccount asdas \
    --InstanceType pulsar \
    --RotateFreq 1440
```

Output: 
```
{
    "Response": {
        "ResetTimestamp": 1774958774848,
        "Status": "Success",
        "TimeCost": 107,
        "Token": "eyJrZXlJZCI6InB1bHNhci1vcDRvZzRqbW96dmsiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhc2RhcyIsImV4cCI6MTc3NTA0NTE3NH0.T5CHC2fuuKg1Z3AylV0MuPhvVG_e4mBhnOSwRQhNakg",
        "RequestId": "fcc38084-db31-47ee-b86f-fbbaed67822c"
    }
}
```

