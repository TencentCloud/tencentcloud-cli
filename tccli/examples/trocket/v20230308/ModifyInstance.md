**Example 1: 修改实例配置**

修改实例配置

Input: 

```
tccli trocket ModifyInstance --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Remark tests \
    --MessageRetention 25
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "becc23c2-b5e1-4df4-9df1-22ba8e5b20c3"
    }
}
```

