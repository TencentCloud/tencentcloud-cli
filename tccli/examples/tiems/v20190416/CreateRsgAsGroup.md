**Example 1: 创建资源组的伸缩组**



Input: 

```
tccli tiems CreateRsgAsGroup --cli-unfold-argument  \
    --Cluster ap-beijing \
    --RsgId rsg-xxxxxxxx \
    --Name asg-xxxxxxxx \
    --MaxSize 5 \
    --MinSize 0 \
    --InstanceType sv_tiems_instance_8c32g1t4
```

Output: 
```
{
    "Response": {
        "RequestId": "3d96e8c0-97a9-43a2-8268-99ff505fbd84",
        "RsgAsGroup": {
            "Id": "asg-xxxxxxxx",
            "Region": "ap-beijing",
            "Zone": "ap-beijing-5",
            "Cluster": "ap-beijing",
            "RsgId": "rsg-xxxxxxxx",
            "Name": "xxxx",
            "MaxSize": 5,
            "MinSize": 0,
            "CreateTime": "2019-12-24T17:39:40+08:00",
            "UpdateTime": "2019-12-24T17:39:40+08:00",
            "Status": "Enabled",
            "InstanceType": "sv_tiems_instance_8c32g1t4",
            "InstanceCount": 0
        }
    }
}
```

