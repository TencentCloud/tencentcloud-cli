**Example 1: 销毁eks**

销毁eks

Input: 

```
tccli cxm TerminateInstances --cli-unfold-argument  \
    --StopType HARD \
    --ForceDestroy False \
    --InstanceIds eks-m9u4q4qh
```

Output: 
```
{
    "Response": {
        "TaskId": 987986917,
        "RequestId": "2295bcd1-2144-4ddd-8052-b6a1bb6d71d0"
    }
}
```

