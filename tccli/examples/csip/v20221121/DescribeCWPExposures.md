**Example 1: 云边界分析列表(适用于主机资产)**



Input: 

```
tccli csip DescribeCWPExposures --cli-unfold-argument  \
    --AssetID ins-2*3r**4u \
    --AssetAppID 260003006 \
    --MemberId mem-0001111 \
    --Limit 1 \
    --Offset 0 \
    --Order DESC \
    --By UpdateTime
```

Output: 
```
{
    "Response": {
        "ExposeList": [
            {
                "AclList": "0.0.0.0/0",
                "AclType": "白名单",
                "AppId": 260083796,
                "AppIdStr": "260083796",
                "AssetId": "lb-iza**f*k",
                "AssetType": "clb_instance",
                "AssetTypeIconSolidURL": "https://cloud-xspm-web-1258344699.cos.ap-guangzhou.myqcloud.com/asset-icon/containerNetworkingIcon_3d.png",
                "AssetTypeIconURL": "https://cloud-xspm-web-1258344699.cos.ap-guangzhou.myqcloud.com/asset-icon/containerNetworkingIcon_2d.svg",
                "AssetTypeName": "负载均衡",
                "CloudAccountId": "700002365149",
                "CloudAccountName": "700002365149",
                "Comment": "",
                "CreateTime": "2026-06-13 04:04:02",
                "DisplayRiskType": "其他",
                "DisplayStatus": "完全开放",
                "Domain": "lb-iza1lfwk-ma*7*p2f5wi9rqtn.clb.gz-*e**entclb*com",
                "ExposureID": 2147503156,
                "HasScan": "false",
                "HighRiskPortServiceCount": 0,
                "InstanceName": "ccs_cls-dqum4px0_tcss-workload-ingress-2",
                "Ip": "",
                "Port": "80",
                "PortDetectCount": 0,
                "PortDetectResult": "",
                "PortServiceCount": 0,
                "Provider": "tencent",
                "RiskType": "other",
                "RiskWebAppCount": 0,
                "ScanTaskStatus": "unknown",
                "Status": "open",
                "Tag": "",
                "ToGovernedRiskContent": "",
                "ToGovernedRiskCount": 0,
                "UpdateTime": "2026-07-01 12:04:00",
                "Uuid": "38638ff07d71eb940627594b753f42ce5c154331",
                "VulCount": 0,
                "WeakPasswordCount": 0,
                "WebAppCount": 0
            }
        ],
        "TotalCount": 18,
        "RequestId": "1f5fe74f-152c-4090-88e0-40342c0b8585"
    }
}
```

