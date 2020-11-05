**Example 1: Terminating Compute Nodes in Batches**



Input: 

```
tccli batch TerminateComputeNodes --cli-unfold-argument  \
    --EnvId env-lcx7qbbr\
    --ComputeNodeId node-lcpcej85 node-lcz8jkvw
```

Output: 
```
{
    "Response": {
        "RequestId": "c50bfbf1-d214-4e41-90f6-39270dc9f071"
    }
}
```

