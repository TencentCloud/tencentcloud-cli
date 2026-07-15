**Example 1: 获取智能体信息列表**



Input: 

```
tccli ccc DescribeAIAgentInfoList --cli-unfold-argument  \
    --SdkAppId 1400692008 \
    --PageSize 1 \
    --PageNumber 5
```

Output: 
```
{
    "Response": {
        "AIAgentInfoList": [
            {
                "AIAgentId": 69,
                "AIAgentName": "u65b0u667au80fdu4f53"
            }
        ],
        "TotalCount": 373,
        "RequestId": "1e6e8974-de10-4485-b53d-25d8c1bef18d"
    }
}
```

