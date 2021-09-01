**Example 1: 添加云主机节点**



Input: 

```
tccli tsf AddInstances --cli-unfold-argument  \
    --InstanceIdList ins-xxxxxxx ins-xxxxxxx \
    --ClusterId cluster-xxxxxxx \
    --InstanceImportMode R \
    --ImageId img-xxxxxxx \
    --Password xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "7b141f81-e708-46f0-a8d3-4e5259c82890",
        "Result": true
    }
}
```

