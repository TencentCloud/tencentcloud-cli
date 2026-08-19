**Example 1: 设置**



Input: 

```
tccli csip ModifyAgentRunPolicy --cli-unfold-argument  \
    --MemberId mem-tencent-54213b157ddf7170 \
    --CustomPolicy.Memory 0 \
    --CustomPolicy.Cpu 40 \
    --CustomPolicy.NetworkPps 200000 \
    --AdvanceModeInstanceIDs ins-8l4a28x6 \
    --CustomModeInstanceIDs ins-fckanelo
```

Output: 
```
{
    "Response": {
        "RequestId": "8912eb2a-1205-441b-b358-78460df01d16"
    }
}
```

