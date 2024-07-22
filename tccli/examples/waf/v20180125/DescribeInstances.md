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
        "Total": 1,
        "Instances": [
            {
                "InstanceId": "abc",
                "InstanceName": "abc",
                "ResourceIds": "abc",
                "Region": "abc",
                "PayMode": 1,
                "RenewFlag": 1,
                "Mode": 1,
                "Level": 1,
                "ValidTime": "abc",
                "BeginTime": "abc",
                "DomainCount": 1,
                "SubDomainLimit": 1,
                "MainDomainCount": 1,
                "MainDomainLimit": 1,
                "MaxQPS": 1,
                "QPS": {
                    "ResourceIds": "abc",
                    "ValidTime": "abc",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": "abc",
                    "BillingItem": "abc"
                },
                "DomainPkg": {
                    "ResourceIds": "abc",
                    "ValidTime": "abc",
                    "RenewFlag": 1,
                    "Count": 1,
                    "Region": "abc"
                },
                "AppId": 1,
                "Edition": "abc",
                "FraudPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "InquireNum": 0,
                    "UsedNum": 0,
                    "RenewFlag": 1
                },
                "BotPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "InquireNum": 0,
                    "UsedNum": 0,
                    "Type": "abc",
                    "RenewFlag": 1,
                    "BotCPWaf": 0,
                    "BotNPWaf": 0,
                    "IsBotTrial": 0
                },
                "BotQPS": {
                    "ResourceIds": "abc",
                    "ValidTime": "abc",
                    "Count": 1,
                    "Region": "abc",
                    "MaxBotQPS": 1,
                    "RenewFlag": 1
                },
                "ElasticBilling": 1,
                "AttackLogPost": 0,
                "MaxBandwidth": 1,
                "APISecurity": 1,
                "QpsStandard": 1,
                "BandwidthStandard": 1,
                "Status": 1,
                "SandboxQps": 1,
                "IsAPISecurityTrial": 1,
                "MajorEventsPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "InquireNum": 0,
                    "UsedNum": 0,
                    "RenewFlag": 1,
                    "BillingItem": "abc",
                    "HWState": 0
                },
                "HybridPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "InquireNum": 0,
                    "UsedNum": 0,
                    "RenewFlag": 1
                },
                "ApiPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "InquireNum": 0,
                    "UsedNum": 0,
                    "RenewFlag": 1,
                    "BillingItem": "abc",
                    "IsAPISecurityTrial": 0
                },
                "MiniPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "Count": 0,
                    "RenewFlag": 1,
                    "BillingItem": "abc"
                },
                "MiniQpsStandard": 1,
                "MiniMaxQPS": 1,
                "LastQpsExceedTime": "abc",
                "MiniExtendPkg": {
                    "ResourceIds": "abc",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "abc",
                    "EndTime": "abc",
                    "Count": 0,
                    "RenewFlag": 1,
                    "BillingItem": "abc"
                },
                "BillingItem": "abc",
                "FreeDelayFlag": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

