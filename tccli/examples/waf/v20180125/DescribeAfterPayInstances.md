**Example 1: 查询后付费基础安全实例列表（含域名与规则实时统计）**

查询后付费基础安全实例列表。Filters 需同时指定 Type 与 Edition；响应中 DomainCount 为实时去重后的接入域名数，ExpertRuleCount 为专家规则数（等于接入域名数），CustomRuleCount 为该实例下所有域名的自定义规则条数之和。

Input: 

```
tccli waf DescribeAfterPayInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Type \
    --Filters.0.Values sp_wsm_waf_pay \
    --Filters.0.ExactMatch True \
    --Filters.1.Name Edition \
    --Filters.1.Values sparta-waf clb-waf \
    --Filters.1.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Instances": [
            {
                "AppId": 251437166,
                "InstanceId": "waf_2l2s8g260autuly7",
                "InstanceName": "gz-postpaid",
                "ResourceIds": "waf_2l2s8g260autuly7",
                "Edition": "sparta-waf",
                "Region": "gz",
                "PayMode": 0,
                "Status": 0,
                "RenewFlag": 0,
                "Level": 203,
                "ValidTime": "2038-01-01 00:00:00",
                "BeginTime": "2026-09-01 10:00:00",
                "ModifyTime": "2026-09-01 10:00:00",
                "BillingItem": "sv_wsm_waf_payg_instance",
                "DomainCount": 17,
                "MainDomainCount": 3,
                "ExpertRuleCount": 17,
                "CustomRuleCount": 10
            }
        ],
        "RequestId": "9f3c1f26-6b7d-4d21-9c2e-2b5f0a71d8e4"
    }
}
```

**Example 2: 查询后付费实例列表**

分页查询后付费实例列表。响应结构与 DescribeInstances 保持一致，复用全量 InstanceDetail（含各类套餐包），并额外填充 LLMTokenUsage。

Input: 

```
tccli waf DescribeAfterPayInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name DealName \
    --Filters.0.Values 20211119002000712600571 \
    --Filters.0.ExactMatch True \
    --FreeDelayFlag 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Instances": [
            {
                "AppId": 251437166,
                "InstanceId": "waf_2l2r0gne0amhqdp3",
                "InstanceName": "gz-Default",
                "ResourceIds": "waf_2l2r0gne0amhqdp3",
                "Edition": "llm-sdk-waf",
                "Region": "gz",
                "PayMode": 0,
                "Status": 0,
                "RenewFlag": 0,
                "AttackLogPost": 0,
                "Level": 201,
                "ElasticBilling": 0,
                "ValidTime": "2038-01-01 00:00:00",
                "BeginTime": "2026-07-06 16:17:09",
                "ModifyTime": "2026-07-06 16:17:09",
                "SubDomainLimit": 0,
                "MainDomainLimit": 0,
                "APISecurity": 0,
                "IsAPISecurityTrial": 0,
                "BillingItem": "sv_wsm_waf_llm_prompt_attack",
                "FreeDelayFlag": 0,
                "BasicFlag": 0,
                "Mode": 0,
                "DomainCount": 0,
                "MainDomainCount": 0,
                "ExpertRuleCount": 0,
                "CustomRuleCount": 0,
                "MaxQPS": 0,
                "MaxBandwidth": 0,
                "QPS": null,
                "BotQPS": null,
                "DomainPkg": null,
                "BotPkg": null,
                "FraudPkg": null,
                "MajorEventsPkg": null,
                "HybridPkg": null,
                "ApiPkg": null,
                "MiniPkg": null,
                "MiniExtendPkg": null,
                "LLMPkg": {
                    "ResourceIds": "waf_2l2r0gne0amhqdp3_0_llm",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2026-07-06 16:17:09",
                    "EndTime": "2038-01-01 00:00:00",
                    "InquireNum": 0,
                    "InquireKey": "sv_wsm_waf_llm_prompt_attack"
                },
                "QpsStandard": 0,
                "BandwidthStandard": 0,
                "SandboxQps": 0,
                "LLMTokenUsage": {
                    "PromptUsage": 1000,
                    "ContentTextUsage": 2000,
                    "SensitiveDataUsage": 500,
                    "ContentImageUsage": 10,
                    "TokenTrend": [
                        {
                            "DayTime": "20260706",
                            "TokenUsage": 3500
                        }
                    ],
                    "ImageTrend": [
                        {
                            "DayTime": "20260706",
                            "ImageUsage": 10
                        }
                    ]
                }
            }
        ],
        "RequestId": "842e99eb-3b4b-4faa-a7d7-7e34e201c3c4"
    }
}
```

