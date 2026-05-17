**Example 1: 查看存储桶调用源ip列表**



Input: 

```
tccli csip DescribeBucketInvokeIpList --cli-unfold-argument  \
    --RelAppId 17223414 \
    --BucketName brain-17223414
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 2131241234,
                "SourceIp": "192.168.1.100",
                "Region": "ap-guangzhou",
                "MarkInfo": "办公网络内部IP",
                "IpType": 1,
                "RelAssetId": "asset-001",
                "RelAssetName": "production-bucket",
                "RelAkCount": 3,
                "RelCosBucketCount": 15,
                "InvokeWay": "api",
                "Uin": "223523525",
                "CsipIpId": "",
                "ISP": "移动",
                "RelCosAlarmInfo": [
                    {
                        "PolicyType": 1,
                        "PolicyTypeName": "公共读取权限风险",
                        "PolicyCount": 5
                    }
                ],
                "LastAccessTime": 1706745600,
                "NickName": "brain"
            }
        ],
        "Total": 156,
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

