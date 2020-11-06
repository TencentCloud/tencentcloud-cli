**Example 1: 修改物理机内网IP**



Input: 

```
tccli bm ModifyLanIp --cli-unfold-argument  \
    --InstanceId cpm-xxxxxxxx \
    --VpcId vpc1 \
    --SubnetId subnet1 \
    --LanIp 10.12.1.2 \
    --RebootDevice 1
```

Output: 
```
{
    "Response": {
        "TaskId": 123,
        "RequestId": "4da5579f-43ff-4ca4-b22a-34b449c8aec7"
    }
}
```

