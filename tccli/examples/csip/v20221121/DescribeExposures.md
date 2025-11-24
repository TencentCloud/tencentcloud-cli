**Example 1: 云边界分析资产列表**



Input: 

```
tccli csip DescribeExposures --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ExposeList": [
            {
                "AclList": "0.0.0.0/0",
                "AclType": "whitelist",
                "AssetId": "ins-bvxns9uy",
                "AssetType": "cvm_instance",
                "AssetTypeName": "云服务器",
                "CloudAccountId": "100010427547",
                "CloudAccountName": "安全攻防",
                "CreateTime": "2024-10-15T07:21:22Z",
                "DisplayRiskType": "非标端口",
                "DisplayStatus": "完全开放",
                "Domain": "",
                "HighRiskPortServiceCount": 0,
                "InstanceName": "tke_cls-5q9sj52q_worker21",
                "Ip": "1.1.1.1",
                "Port": "30000-32768",
                "PortServiceCount": 0,
                "Provider": "腾讯云",
                "RiskType": "no_standard_port",
                "RiskWebAppCount": 0,
                "Status": "open",
                "UpdateTime": "2025-01-14T02:31:55Z",
                "VulCount": 0,
                "WeakPasswordCount": 0,
                "WebAppCount": 0,
                "ScanTaskStatus": "running",
                "Uuid": "sadsds",
                "HasScan": "true",
                "AppId": 12465129,
                "Tag": "",
                "ToGovernedRiskContent": "",
                "ToGovernedRiskCount": 0,
                "ExposureID": 1,
                "PortDetectCount": 2
            }
        ],
        "RequestId": "0ce09587-eaba-4f70-ae9b-1a80b69ee21f",
        "TotalCount": 102
    }
}
```

