**Example 1: 修改容器部署组实例数**



Input: 

```
tccli tsf ModifyContainerReplicas --cli-unfold-argument  \
    --GroupId group-xxxxxxx \
    --InstanceNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b435457b-9a52-484c-bbbd-fc31dcd0d021",
        "Result": true
    }
}
```

