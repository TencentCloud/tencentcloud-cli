**Example 1: 创建敏捷上云服务**

创建敏捷上云服务

Input: 

```
tccli dc CreateCloudAttachService --cli-unfold-argument  \
    --Data.Name 我的实例01 \
    --Data.IdcAddress 北京东城区IDC地址 \
    --Data.IdcType CUCC \
    --Data.Bandwidth 100 \
    --Data.Telephone 18888888888 \
    --Data.Remarks 字符串
```

Output: 
```
{
    "Response": {
        "CloudAttach": {
            "Uin": "100001332514",
            "CustomerAuthName": "网测技术",
            "InstanceId": "cas-3vocyz07",
            "Name": "我的实例01",
            "AppId": "1254277469",
            "IapId": "",
            "IdcAddress": "北京东城区IDC地址",
            "IdcType": "CUCC",
            "DirectConnectId": "",
            "CloudAttachServiceGatewaysSupport": false,
            "BUpdateBandwidth": false,
            "Bandwidth": 100,
            "RegionStatus": "same-region",
            "Status": "applying",
            "ApplyTime": "2024-10-14 13:04:33",
            "ReadyTime": "2038-01-08 23:59:59",
            "ExpireTime": "2038-01-08 23:59:59",
            "Telephone": "18888888888",
            "Remarks": "6个月，其他"
        },
        "RequestId": "4fb676d2-3100-4018-aa07-73008eaa135d"
    }
}
```

