**Example 1: Changing the Number of Desired Nodes in a Compute Environment to 2**



Input: 

```
tccli batch ModifyComputeEnv --cli-unfold-argument  \
    --EnvId env-lcpcej85\
    --DesiredComputeNodeCount 2
```

Output: 
```
{
    "Response": {
        "RequestId": "147fbf83-f817-4528-a547-f5f313b673d2"
    }
}
```

