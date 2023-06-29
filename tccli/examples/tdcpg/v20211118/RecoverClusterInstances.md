**Example 1: 恢复实例**



Input: 

```
tccli tdcpg RecoverClusterInstances --cli-unfold-argument  \
    --ClusterId tdcpg-77iesdqa \
    --InstanceIdSet tdcpg-ins-pzu77n6e tdcpg-ins-7llxkcbg \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e0ef1b06-405f-48cc-863f-185dbb6eb037"
    }
}
```

