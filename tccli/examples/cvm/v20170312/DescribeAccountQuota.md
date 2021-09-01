**Example 1: 查询用户概览数据**

查询用户云主机、各个地域配额等数据。

Input: 

```
tccli cvm DescribeAccountQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccountQuotaOverview": {
            "Region": "ap-guangzhou",
            "AccountQuota": {
                "PostPaidQuotaSet": [
                    {
                        "UsedQuota": 0,
                        "RemainingQuota": 288,
                        "TotalQuota": 288,
                        "Zone": "ap-guangzhou-1"
                    },
                    {
                        "UsedQuota": 2,
                        "RemainingQuota": 1248,
                        "TotalQuota": 1250,
                        "Zone": "ap-guangzhou-2"
                    }
                ],
                "DisasterRecoverGroupQuotaSet": [
                    {
                        "CvmInRackGroupQuota": 30,
                        "GroupQuota": 10,
                        "CvmInHostGroupQuota": 50,
                        "CurrentNum": 0,
                        "CvmInSwitchGroupQuota": 20
                    }
                ],
                "PrePaidQuotaSet": [
                    {
                        "UsedQuota": 0,
                        "OnceQuota": 300,
                        "Zone": "ap-guangzhou-1",
                        "TotalQuota": 255,
                        "RemainingQuota": 255
                    },
                    {
                        "UsedQuota": 0,
                        "OnceQuota": 300,
                        "Zone": "ap-guangzhou-2",
                        "TotalQuota": 222,
                        "RemainingQuota": 222
                    }
                ],
                "SpotPaidQuotaSet": [
                    {
                        "UsedQuota": 0,
                        "RemainingQuota": 244,
                        "TotalQuota": 244,
                        "Zone": "ap-guangzhou-1"
                    },
                    {
                        "UsedQuota": 4,
                        "RemainingQuota": 195,
                        "TotalQuota": 199,
                        "Zone": "ap-guangzhou-2"
                    }
                ],
                "ImageQuotaSet": [
                    {
                        "UsedQuota": 0,
                        "TotalQuota": 10
                    }
                ]
            }
        },
        "RequestId": "7f117776-3d20-4f00-839b-b22b04625f47",
        "AppId": 251007416
    }
}
```

