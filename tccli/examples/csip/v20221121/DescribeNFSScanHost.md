**Example 1: 获取NFS扫描配置机器列表**

获取NFS扫描配置机器列表

Input: 

```
tccli csip DescribeNFSScanHost --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --Order ASC \
    --By Id
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "FunctionStatus": 1,
                "Id": 534012791,
                "InstanceId": "lhins***iylm",
                "InstanceStatus": "RUNNING",
                "MachineExtraInfo": {
                    "HostName": "u9075u9f99-u***4bu8bd5u7528",
                    "InstanceID": "lhins***iylm",
                    "NetworkName": "vpc-***kfai",
                    "NetworkType": 1,
                    "PrivateIP": "10.***0.2",
                    "WanIP": "82.15***.223"
                },
                "Message": "",
                "MessageDesc": "",
                "Name": "u9075u9f99-u***4bu8bd5u7528",
                "PrivateIp": "10.***0.2",
                "PublicIp": "82.15***.223",
                "Quuid": "15c76928-e4e***46c7de784744",
                "RegionInfo": {
                    "Region": "ap-b***ing",
                    "RegionCode": "bj",
                    "RegionId": 8,
                    "RegionName": "u534eu5317u***u5317u4eac)",
                    "RegionNameEn": "North C***eijing)"
                },
                "Status": "OFFLINE",
                "VpcId": "vpc-***kfai"
            }
        ],
        "Total": 8,
        "RequestId": "33d0b5f0-130a-470e-9fee-3c37234a17c9"
    }
}
```

