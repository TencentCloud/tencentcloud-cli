**Example 1: 复制组实例更换角色**



Input: 

```
tccli redis ChangeInstanceRole --cli-unfold-argument  \
    --GroupId crs-rpl-267khx71 \
    --InstanceId crs-5qlrlhux \
    --InstanceRole rw
```

Output: 
```
{
    "Response": {
        "TaskId": 327,
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

