**Example 1: 资源与配额详情**

概览页资源与配额详情抽屉

Input: 

```
tccli cfw DescribeOverviewResourceQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Detail": {
                "EastWestDetail": {
                    "AllocatedBandwidthUsedMbps": 2048,
                    "CanUsedBandwidthMbps": 2500,
                    "ClusterModeWidthMbps": 452,
                    "ClusterVpcMaxFlowBps": 25484,
                    "DiffRegionFwInsId": "",
                    "DiffRegionFwInsName": "",
                    "DiffRegionMaxFlowBps": 0,
                    "FwGroupId": "cfwg-8f6785ee",
                    "FwGroupMaxFlowBps": 1697845555,
                    "FwGroupName": "自动化",
                    "FwInsId": "cfwew-46cfffdc",
                    "FwInsMaxFlowBps": 1697845555,
                    "FwInsName": "自动化-上海",
                    "MasterSlaveModeWidthMbps": 2048,
                    "SameRegionFwInsId": "",
                    "SameRegionFwInsName": "",
                    "SameRegionMaxFlowBps": 0,
                    "TotalMbps": 2500,
                    "UsagePercent": 0.647676679611206,
                    "UsedBps": 1697845555
                },
                "LogStorageDetail": {
                    "AclSize": 7088386412,
                    "ArrearsStopWriting": 0,
                    "IdsSize": 825949749,
                    "NDRNetFlowSize": 37625103293,
                    "NDRRiskSize": 1876072,
                    "NDRStorageDay": 730,
                    "NetFlowSize": 30811297507,
                    "OperateSize": 55808837,
                    "PayMode": 1,
                    "StorageDay": 730,
                    "TotalBytes": 5368709120000,
                    "UsedBytes": 76408421870
                },
                "NDRDetail": {
                    "FlowPercent": 0.019475028850138187,
                    "InMaxBps": 41339813,
                    "MaxFlowBps": 41822306,
                    "OutMaxBps": 1598034,
                    "Status": 1,
                    "TotalMbps": 2048
                },
                "NorthSouthDetail": {
                    "BypassOnlyBandwidthMbps": 0,
                    "CanUsedBandwidthMbps": 300,
                    "InternetBandwidthTotalMbps": 300,
                    "MaxSerialRegion": "eu-frankfurt",
                    "NatBandwidthTotalMbps": 40,
                    "NetMaxFlowBps": 676507327,
                    "SerialBandwidthTotalMbps": 90,
                    "SerialRegionInFlowMax": 109794282,
                    "SerialRegionOutFlowMax": 11110480,
                    "UnusedBandwidthMbps": 0
                },
                "QuotaDetail": {
                    "AccessControlRuleTotal": 15000,
                    "AccessControlRuleUsed": 9,
                    "AddressTemplateTotal": 530,
                    "AddressTemplateUsed": 493,
                    "BlockIpCount": 13,
                    "BlockIpTotal": 20100,
                    "BlockIpUsed": 13,
                    "BlockListQuota": {
                        "InUsedCnt": 10,
                        "OutUsedCnt": 3,
                        "TotalCnt": 20100,
                        "UsedCnt": 13
                    },
                    "BlockListQuotaDetail": {
                        "BaseRemainCnt": 19987,
                        "BaseTotalCnt": 20000,
                        "BaseUsedCnt": 13,
                        "ExtensionRemainCnt": 100,
                        "ExtensionTotalCnt": 100,
                        "ExtensionUsedCnt": 0,
                        "RemainCnt": 20087,
                        "TotalCnt": 20100,
                        "UsedCnt": 13
                    },
                    "BorderRuleQuota": {
                        "AllowedNum": 5000,
                        "InEnableNum": 0,
                        "InTotal": 0,
                        "OutEnableNum": 6,
                        "OutTotal": 7,
                        "RemainExtensionNum": 100,
                        "RemainQuota": 5093,
                        "UsedNum": 7
                    },
                    "CommonInstanceRemain": 12,
                    "CommonInstanceTotal": 20,
                    "CommonInstanceUsed": 8,
                    "HoneyPotTotal": 10,
                    "HoneyPotUsed": 4,
                    "NatInstanceUsed": 4,
                    "NatRuleQuota": {
                        "AllowedNum": 5000,
                        "InEnableNum": 1,
                        "InTotal": 1,
                        "OutEnableNum": 0,
                        "OutTotal": 0,
                        "RemainExtensionNum": 100,
                        "RemainQuota": 5099,
                        "UsedNum": 1
                    },
                    "PublicIpTotal": 1124,
                    "PublicIpUsed": 37,
                    "SerialRegionUsed": 5,
                    "SgRuleQuotaTotal": 2000,
                    "SgRuleQuotaUsed": 16,
                    "TotalExtensionNum": 100,
                    "TotalExtensionUsed": 0,
                    "VpcInstanceUsed": 4,
                    "VpcRuleQuota": {
                        "AllowedNum": 5000,
                        "EdgeEnableRuleNum": 0,
                        "EdgeRuleNum": 0,
                        "GlobalEnableRuleNum": 1,
                        "GlobalRuleNum": 1,
                        "IsSwitchEnable": 1,
                        "RemainExtensionNum": 100,
                        "RemainQuota": 5099,
                        "UsedNum": 1,
                        "V4EnableRuleTotal": 1,
                        "V4RuleTotal": 1,
                        "V6EnableRuleTotal": 0,
                        "V6RuleTotal": 0
                    }
                }
            }
        },
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "8e5ce370-585b-4fab-8635-5977d44ad905"
    }
}
```

