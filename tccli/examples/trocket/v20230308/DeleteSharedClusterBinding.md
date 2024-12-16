**Example 1: 删除成功**

删除成功响应

Input: 

```
tccli trocket DeleteSharedClusterBinding --cli-unfold-argument  \
    --ClusterId rmq5-room-cd-1 \
    --BindingUin 123 \
    --InstanceTypes EXPERIMENT
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "2e229253-d9c4-4e2c-8cec-d2b327963a85"
    }
}
```

