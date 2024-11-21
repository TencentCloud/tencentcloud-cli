**Example 1: 查询用户所有实例的详细信息**

查询用户所有实例的详细信息

Input: 

```
tccli waf DescribeInstances --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Filters.0.Name Edition \
    --Filters.0.ExactMatch True \
    --Filters.1.Name Region \
    --Filters.1.Values ap-beijing ap-guangzhou \
    --Filters.1.ExactMatch True \
    --Filters.2.Name InstanceName \
    --Filters.2.Values 实例 \
    --Filters.2.ExactMatch False \
    --Filters.3.Name InstanceId \
    --Filters.3.Values waf \
    --Filters.3.ExactMatch False
```

Output: 
```
{
    "Response": {
        "RequestId": "d206a27c-2c9c-4ac8-a9e0-6cdf4703247c",
        "Total": 2,
        "Instances": [
            {
                "AppId": 87524381,
                "InstanceId": "waf_2kw60zgy0908e8j3",
                "InstanceName": "广州双栈集群企业版",
                "ResourceIds": "waf_2kw60zgy0908e8j3",
                "Edition": "sparta-waf",
                "Region": "gz",
                "PayMode": 1,
                "Status": 0,
                "RenewFlag": 1,
                "AttackLogPost": 1,
                "Level": 3,
                "ElasticBilling": 100000,
                "ValidTime": "2024-11-01 15:27:23",
                "BeginTime": "2022-09-01 15:27:23",
                "SubDomainLimit": 30,
                "MainDomainLimit": 3,
                "APISecurity": 1,
                "IsAPISecurityTrial": 0,
                "BillingItem": "sv_wsm_waf_package_enterprise",
                "FreeDelayFlag": 0,
                "Mode": 1,
                "DomainCount": 19,
                "MainDomainCount": 3,
                "MaxQPS": 50,
                "MaxBandwidth": 203021,
                "QPS": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_qps",
                    "ValidTime": "2024-11-01 15:27:23",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": "gz",
                    "BillingItem": "sv_wsm_waf_package_enterprise"
                },
                "BotQPS": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_botqps",
                    "ValidTime": "2024-11-01 15:27:23",
                    "Count": 0,
                    "Region": "gz",
                    "MaxBotQPS": 50,
                    "RenewFlag": 0
                },
                "DomainPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_domain",
                    "ValidTime": "2024-11-01 15:27:23",
                    "RenewFlag": 0,
                    "Count": 1,
                    "Region": "gz"
                },
                "BotPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_bot",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2022-01-05 15:38:04",
                    "EndTime": "2025-01-15 15:38:04",
                    "Type": "sv_wsm_waf_scene_bot",
                    "InquireNum": 1,
                    "UsedNum": 0,
                    "RenewFlag": 0,
                    "BotCPWaf": 0,
                    "BotNPWaf": 0,
                    "IsBotTrial": 0
                },
                "FraudPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_fraud",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-06-19 19:22:59",
                    "EndTime": "2024-11-01 19:22:59",
                    "InquireNum": 5000,
                    "UsedNum": 37,
                    "RenewFlag": 1
                },
                "MajorEventsPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_major_events",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-05-16 16:57:16",
                    "EndTime": "2024-08-16 16:57:16",
                    "InquireNum": 1000,
                    "UsedNum": 0,
                    "BillingItem": "sv_wsm_waf_scene_major_events_basic",
                    "RenewFlag": 0,
                    "HWState": 3
                },
                "HybridPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_hcn",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "2024-05-16 16:57:16",
                    "EndTime": "2024-08-16 16:57:16",
                    "InquireNum": 0,
                    "UsedNum": 0,
                    "RenewFlag": 0
                },
                "ApiPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_api",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-04-23 00:01:51",
                    "EndTime": "2024-11-01 00:01:51",
                    "InquireNum": 1,
                    "UsedNum": 0,
                    "BillingItem": "sv_wsm_waf_scene_ent",
                    "RenewFlag": 1,
                    "IsAPISecurityTrial": 0
                },
                "MiniPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_1_mini",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-04-11 11:31:01",
                    "EndTime": "2024-11-01 11:31:01",
                    "Count": 5,
                    "BillingItem": "sv_wsm_waf_scene_mini",
                    "RenewFlag": 1
                },
                "MiniExtendPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_0_mini_extend",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-05-30 23:35:08",
                    "EndTime": "2024-11-01 23:35:08",
                    "Count": 1,
                    "BillingItem": "sv_wsm_waf_exp_exp",
                    "RenewFlag": 1
                },
                "QpsStandard": 105000,
                "BandwidthStandard": 2600,
                "SandboxQps": 115000,
                "LastQpsExceedTime": "2024-11-01 23:35:08",
                "MiniQpsStandard": 473500,
                "MiniMaxQPS": 1
            },
            {
                "AppId": 87524381,
                "InstanceId": "waf_2kuil2fm02vqm7z3",
                "InstanceName": "gz-Default1",
                "ResourceIds": "waf_2kuil2fm02vqm7z3",
                "Edition": "clb-waf",
                "Region": "cd,cq,gz,bj",
                "PayMode": 1,
                "Status": 0,
                "RenewFlag": 1,
                "AttackLogPost": 1,
                "Level": 3,
                "ElasticBilling": 2510000,
                "ValidTime": "2024-11-28 16:35:25",
                "BeginTime": "2021-09-17 16:35:25",
                "SubDomainLimit": 130,
                "MainDomainLimit": 13,
                "APISecurity": 1,
                "IsAPISecurityTrial": 0,
                "BillingItem": "sv_wsm_waf_package_enterprise_clb",
                "FreeDelayFlag": 0,
                "Mode": 0,
                "DomainCount": 24,
                "MainDomainCount": 6,
                "MaxQPS": 24,
                "MaxBandwidth": 52091,
                "QPS": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_qps",
                    "ValidTime": "2024-11-18 21:22:10",
                    "RenewFlag": 1,
                    "Count": 1000,
                    "Region": "gz",
                    "BillingItem": "sv_wsm_waf_qps_ep_clb"
                },
                "BotQPS": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_0_botqps",
                    "ValidTime": "2024-11-01 15:27:23",
                    "Count": 0,
                    "Region": "gz",
                    "MaxBotQPS": 50,
                    "RenewFlag": 0
                },
                "DomainPkg": {
                    "ResourceIds": "waf_2kw60zgy0908e8j3_domain",
                    "ValidTime": "2024-11-01 15:27:23",
                    "RenewFlag": 0,
                    "Count": 1,
                    "Region": "gz"
                },
                "BotPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_0_bot",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2022-01-05 15:38:04",
                    "EndTime": "2022-01-15 15:38:04",
                    "Type": "sv_wsm_waf_scene_bot",
                    "InquireNum": 1,
                    "UsedNum": 0,
                    "RenewFlag": 0,
                    "BotCPWaf": 0,
                    "BotNPWaf": 0,
                    "IsBotTrial": 0
                },
                "FraudPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_0_fraud",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-06-19 19:22:59",
                    "EndTime": "2024-11-01 19:22:59",
                    "InquireNum": 5000,
                    "UsedNum": 37,
                    "RenewFlag": 1
                },
                "MajorEventsPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_0_major_events",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-05-16 16:57:16",
                    "EndTime": "2024-08-16 16:57:16",
                    "InquireNum": 1000,
                    "UsedNum": 0,
                    "BillingItem": "sv_wsm_waf_scene_major_events_basic",
                    "RenewFlag": 0,
                    "HWState": 3
                },
                "HybridPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_0_hcn",
                    "Status": 0,
                    "Region": 1,
                    "BeginTime": "2023-09-29 11:16:20",
                    "EndTime": "2024-09-29 11:16:20",
                    "InquireNum": 1,
                    "UsedNum": 0,
                    "RenewFlag": 0
                },
                "ApiPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_api",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2023-11-06 20:34:31",
                    "EndTime": "2024-11-18 16:35:25",
                    "InquireNum": 1,
                    "UsedNum": 0,
                    "BillingItem": "sv_wsm_waf_scene_cent",
                    "RenewFlag": 1,
                    "IsAPISecurityTrial": 0
                },
                "MiniPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_1_mini",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-04-11 11:31:01",
                    "EndTime": "2024-11-01 11:31:01",
                    "Count": 5,
                    "BillingItem": "sv_wsm_waf_scene_mini",
                    "RenewFlag": 1
                },
                "MiniExtendPkg": {
                    "ResourceIds": "waf_2kuil2fm02vqm7z3_0_mini_extend",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2024-05-30 23:35:08",
                    "EndTime": "2024-11-01 23:35:08",
                    "Count": 1,
                    "BillingItem": "sv_wsm_waf_exp_exp",
                    "RenewFlag": 1
                },
                "QpsStandard": 11000,
                "BandwidthStandard": 350,
                "SandboxQps": 18000,
                "LastQpsExceedTime": "2024-11-01 23:35:08",
                "MiniQpsStandard": 0,
                "MiniMaxQPS": 0
            }
        ]
    }
}
```

