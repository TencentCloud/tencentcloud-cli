**Example 1: 根据消费者筛选**



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
                            "ConsumerGroupId": "cg-3155bd3c9fd0df",
                            "Name": "test-consumer-group-1"
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

**Example 2: 根据消费者组筛选**



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

