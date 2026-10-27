**Example 1: 成功-消费者组（组织节点）维度**

按消费者组（组织节点）聚合 Token 用量；适用于网关版本不低于 3.9.8。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMTokenUsageList --cli-unfold-argument  \
    --GatewayId gateway-0663f44f \
    --StartTime 1789603200 \
    --EndTime 1789689600 \
    --Dimension ConsumerGroup \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Name ConsumerGroupId \
    --Filters.0.Values 00000000-0000-0000-0000-000000000012
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "ConsumerId": "",
                    "ConsumerName": "",
                    "ConsumerGroups": [],
                    "ModelServiceId": "",
                    "ModelServiceName": "",
                    "DimensionList": [
                        {
                            "Key": "ConsumerGroupId",
                            "Values": [
                                "00000000-0000-0000-0000-000000000012"
                            ]
                        },
                        {
                            "Key": "ConsumerGroupName",
                            "Values": [
                                "平台组"
                            ]
                        },
                        {
                            "Key": "MemberCount",
                            "Values": [
                                "3"
                            ]
                        },
                        {
                            "Key": "ConsumerGroupPath",
                            "Values": [
                                "自定义组织架构 / 研发部 / 平台组"
                            ]
                        }
                    ],
                    "InputTokens": 10000,
                    "CacheReadInputTokens": 2000,
                    "OutputTokens": 3000,
                    "TotalTokens": 13000,
                    "RequestCount": 10,
                    "Currency": "CNY"
                }
            ],
            "TotalCount": 1,
            "OrgAttributionIncomplete": false
        },
        "RequestId": "request-example"
    }
}
```

**Example 2: 根据消费者筛选**

未传 Dimension，返回消费者与模型服务二维列表；3.9.8 起消费者组信息包含当前组织路径。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMTokenUsageList --cli-unfold-argument  \
    --GatewayId gateway-0663f44f \
    --StartTime 1779638400 \
    --EndTime 1779690592 \
    --Filters.0.Name ConsumerId \
    --Filters.0.Values 2e36f421-e08f-4e9e-a610-1b1f84c9cb6d \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "CacheReadInputTokens": 0,
                    "ConsumerGroups": [
                        {
                            "ConsumerGroupId": "00000000-0000-0000-0000-000000000012",
                            "Name": "平台组",
                            "ConsumerGroupPath": "自定义组织架构 / 研发部 / 平台组"
                        }
                    ],
                    "ConsumerId": "2e36f421-e08f-4e9e-a610-1b1f84c9cb6d",
                    "ConsumerName": "test-consumer-2",
                    "Cost": "0.00",
                    "Currency": "CNY",
                    "InputTokens": 45,
                    "ModelServiceId": "b97facfd14724ccea64358fd1769b784",
                    "ModelServiceName": "qwen",
                    "OutputTokens": 11,
                    "RequestCount": 2,
                    "TotalTokens": 56
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "79a1003e-8d6f-4b14-a61e-b04c4f9e004b"
    }
}
```

**Example 3: 根据消费者组筛选**

旧版本消费者组 ID 筛选示例；未传 Dimension，仍按当前成员筛选。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMTokenUsageList --cli-unfold-argument  \
    --GatewayId gateway-0663f44f \
    --StartTime 1779638400 \
    --EndTime 1779690592 \
    --Filters.0.Name ConsumerGroupId \
    --Filters.0.Values cg-6e111dd2fc5cee \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "CacheReadInputTokens": 0,
                    "ConsumerGroups": [
                        {
                            "ConsumerGroupId": "cg-6e111dd2fc5cee",
                            "Name": "test-consumer-group-2"
                        }
                    ],
                    "ConsumerId": "2e36f421-e08f-4e9e-a610-1b1f84c9cb6d",
                    "ConsumerName": "test-consumer-2",
                    "Cost": "0.00",
                    "Currency": "CNY",
                    "InputTokens": 45,
                    "ModelServiceId": "b97facfd14724ccea64358fd1769b784",
                    "ModelServiceName": "qwen",
                    "OutputTokens": 11,
                    "RequestCount": 2,
                    "TotalTokens": 56
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "dff1a641-28ea-4c7f-91cc-c89467dc70ef"
    }
}
```

