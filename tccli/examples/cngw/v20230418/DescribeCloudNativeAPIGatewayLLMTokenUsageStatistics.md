**Example 1: 成功-查询全部消费者与消费者组**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --StartTime 1777996800 \
    --EndTime 1778688000
```

Output: 
```
{
    "Response": {
        "Result": {
            "Currency": "CNY",
            "TopConsumers": [
                {
                    "ConsumerName": "test-consumer-1",
                    "TotalTokens": 2685
                }
            ],
            "TotalCachedReadInputTokens": 0,
            "TotalCost": "0.077996",
            "TotalInputTokens": 222,
            "TotalOutputTokens": 3262,
            "TotalRequestCount": 19
        },
        "RequestId": "46f2429e-db7f-48f3-a028-634d7f861ee5"
    }
}
```

**Example 2: 成功-根据消费者组过滤**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics --cli-unfold-argument  \
    --GatewayId gateway-0663f44f \
    --StartTime 1779638400 \
    --EndTime 1779690592 \
    --Filters.0.Name ConsumerGroupId \
    --Filters.0.Values cg-6e111dd2fc5cee
```

Output: 
```
{
    "Response": {
        "Result": {
            "Currency": "CNY",
            "TopConsumers": [
                {
                    "ConsumerId": "2e36f421-e08f-4e9e-a610-1b1f84c9cb6d",
                    "ConsumerName": "test-consumer-2",
                    "TotalTokens": 56
                }
            ],
            "TotalCachedReadInputTokens": 0,
            "TotalCost": "0.0",
            "TotalInputTokens": 45,
            "TotalOutputTokens": 11,
            "TotalRequestCount": 2
        },
        "RequestId": "6ac1d99b-58a9-42df-82a0-78d53c63aa31"
    }
}
```

**Example 3: 成功-根据消费者过滤**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics --cli-unfold-argument  \
    --GatewayId gateway-0663f44f \
    --StartTime 1777996800 \
    --EndTime 1778774400 \
    --Filters.0.Name ConsumerId \
    --Filters.0.Values 2e36f421-e08f-4e9e-a610-1b1f84c9cb6d
```

Output: 
```
{
    "Response": {
        "Result": {
            "Currency": "CNY",
            "TopConsumers": [
                {
                    "ConsumerName": "test-consumer-2",
                    "TotalTokens": 619
                }
            ],
            "TotalCachedReadInputTokens": 0,
            "TotalCost": "0.006118",
            "TotalInputTokens": 48,
            "TotalOutputTokens": 571,
            "TotalRequestCount": 3
        },
        "RequestId": "36ffccea-99cc-4cc0-97ef-f9dd0b45c377"
    }
}
```

