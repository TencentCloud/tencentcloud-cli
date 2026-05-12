**Example 1: 创建敏捷上云服务**

创建敏捷上云服务

Input: 

```
tccli dc CreateCloudAttachService --cli-unfold-argument  \
    --Data.Name 测试线路名 \
    --Data.IdcAddress 湖北省武汉市高薪大道xx机房xxx地址 \
    --Data.IdcType CUCC \
    --Data.Bandwidth 100 \
    --Data.Telephone 13888888888 \
    --Data.Remarks None \
    --Data.ArRegion gz \
    --Data.IdcPointType CLOUD \
    --Data.BIapLinkProtected True \
    --Data.ServiceType SHARE
```

Output: 
```
{
    "Response": {
        "CloudAttach": {
            "AppId": "251202094",
            "ApplyTime": "2026-04-17 17:26:52",
            "ArRegion": "gz",
            "BIapLinkProtected": true,
            "BUpdateBandwidth": false,
            "Bandwidth": 100,
            "CloudAttachServiceGatewaysSupport": false,
            "CustomerAuthName": "客户名称",
            "DirectConnectId": "",
            "ExpireTime": "2038-01-08 23:59:59",
            "IapId": "",
            "IdcAddress": "湖北省武汉市高薪大道xx机房xxx地址",
            "IdcPointType": "CLOUD",
            "IdcType": "CUCC",
            "InstanceId": "aoc-cigdpnb5",
            "Name": "测试线路名",
            "ReadyTime": null,
            "RegionStatus": "same-region",
            "Remarks": "",
            "ServiceType": "SHARE",
            "Status": "applying",
            "Telephone": "13888888888",
            "Uin": "700000161058",
            "VlanRange": ""
        },
        "RequestId": "ba33a478-e39a-4e1f-8cc8-2f46981e896e"
    }
}
```

