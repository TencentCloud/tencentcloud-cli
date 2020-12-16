**Example 1: 修改节点池关联伸缩组的期望实例数示例**



Input: 

```
tccli tke ModifyNodePoolDesiredCapacityAboutAsg --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --NodePoolId np-xxx \
    --DesiredCapacity 6
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

