**Example 1: 修改节点池关联伸缩组的期望实例数示例**

修改节点池关联伸缩组的期望实例数示例

Input: 

```
tccli tke ModifyNodePoolDesiredCapacityAboutAsg --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --DesiredCapacity 6 \
    --NodePoolId np-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

