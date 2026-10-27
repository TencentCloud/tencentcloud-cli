**Example 1: DescribeInstances**



Input: 

```
tccli cvd DescribeInstances --cli-unfold-argument  \
    --PageNumber 1 \
    --Filters.0.Values Region \
    --Filters.0.Name ap-shanghai \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "InstanceId": "cdi-0s9hw",
                "Name": "0s9hw",
                "Status": "STOPPED",
                "UserName": "xxa",
                "UserId": "xxa",
                "InstanceType": "S1LARGE8",
                "SysDisk": {
                    "DiskType": "CLOUD_SSD",
                    "DiskSize": 0,
                    "DiskId": "disk1"
                },
                "DataDiskList": [
                    {
                        "DiskType": "CLOUD_SSD",
                        "DiskSize": 0,
                        "DiskId": "disk2"
                    }
                ],
                "Region": "ap-shanghai",
                "ChargeType": "POSTPAID_BY_HOUR",
                "AutoRenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "Description": "",
                "HostName": "0s9hw",
                "DisplayName": "0s9hw",
                "BindStatus": "UNBOUND",
                "ImageId": "image-1",
                "UserVpcId": "vpc-1",
                "UserSubnetId": "subnet-1",
                "UserPrivateIp": "0.0.0.0",
                "IsolatedTime": "2020-09-22T00:00:00+00:00",
                "LastStatusChangeReason": "",
                "LatestOperation": "",
                "LatestOperationState": "",
                "LatestOperationRequestID": "",
                "OsName": "Windows Server",
                "SetId": "",
                "AppId": 0,
                "Uin": "1******43",
                "SecurityGroups": [
                    "sg1"
                ]
            }
        ],
        "Total": 0,
        "RequestId": "abc-avc"
    }
}
```

