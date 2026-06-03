**Example 1: 应用服务关联列表查询**



Input: 

```
tccli apis DescribeAgentAppServices --cli-unfold-argument  \
    --InstanceID ins-222fd0da \
    --Limit 10 \
    --IDs aga-cc2448c0-svr-17244a65 \
    --AgentAppIDs aga-cc2448c0 \
    --ServiceIDs svr-17244a65 \
    --Keyword 43343 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "Total": 0
        },
        "RequestId": "793c8738-5922-4ef2-92ca-dc93bd0b6cf3"
    }
}
```

