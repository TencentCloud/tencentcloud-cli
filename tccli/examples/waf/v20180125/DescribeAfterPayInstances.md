**Example 1: 查询后付费实例列表**

分页查询 Edition=llm-sdk-waf 的后付费实例列表，可按子订单号（Name=DealName）过滤；返回实例基础信息及 LLM 资源包、当天各模块 token 消耗量与近 7 天趋势。

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
                "ValidTime": "2038-01-01 00:00:00",
                "BeginTime": "2026-07-06 16:17:09",
                "BillingItem": "sv_wsm_waf_llm_prompt_attack",
                "RenewFlag": 0,
                "Level": 201,
                "ModifyTime": "2026-07-06 16:17:09",
                "SubDomainLimit": 0,
                "MainDomainLimit": 0,
                "ElasticBilling": 0,
                "AttackLogPost": 0,
                "APISecurity": 0,
                "IsAPISecurityTrial": 0,
                "FreeDelayFlag": 0,
                "BasicFlag": 0,
                "LLMPkg": {
                    "ResourceIds": "waf_2l2r0gne0amhqdp3_0_llm",
                    "Status": 1,
                    "Region": 1,
                    "BeginTime": "2026-07-06 16:17:09",
                    "EndTime": "2038-01-01 00:00:00",
                    "InquireNum": 0,
                    "InquireKey": "sv_wsm_waf_llm_prompt_attack"
                },
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

