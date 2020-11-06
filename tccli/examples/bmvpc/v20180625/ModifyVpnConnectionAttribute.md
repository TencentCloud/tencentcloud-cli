**Example 1: 修改VPN通道**



Input: 

```
tccli bmvpc ModifyVpnConnectionAttribute --cli-unfold-argument  \
    --Version 2018-06-25 \
    --VpnConnectionId bmvpnx-qc8cz8y8 \
    --VpnConnectionName TEST_CONN \
    --VpcId vpc-q8cz9732
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "09186e64-d19e-4ca1-968f-df4fc8139192"
    }
}
```

