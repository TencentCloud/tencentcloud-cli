**Example 1: 添加成功**

添加成功响应

Input: 

```
tccli trocket CreateSharedClusterBinding --cli-unfold-argument  \
    --ClusterId rmq5-room-cd-1 \
    --Enabled True \
    --Remark dev \
    --BindingUin 123 \
    --InstanceTypes EXPERIMENT
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "94f23822-0f55-4930-8a31-abb84f3b2480"
    }
}
```

