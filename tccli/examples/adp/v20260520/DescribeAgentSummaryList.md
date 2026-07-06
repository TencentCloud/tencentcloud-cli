**Example 1: 查询指定应用下Agent列表**



Input: 

```
tccli adp DescribeAgentSummaryList --cli-unfold-argument  \
    --Scope 0 \
    --AppId 206*************168
```

Output: 
```
{
    "Response": {
        "AgentList": [
            {
                "AdvancedConfig": {
                    "MaxReasoningRound": 100
                },
                "AgentId": "405abc07-438d-4293-90aa-3933c2ed2a80",
                "Profile": {
                    "AppName": "",
                    "Description": "",
                    "Developer": "",
                    "IconUrl": "https://cdn.xiaowei.qq.com/static/lke/agent-robot.png",
                    "Name": "hu******aw",
                    "Role": 0
                }
            }
        ],
        "TotalCount": 2,
        "RequestId": "0c2b804e-7835-4c4a-a8d5-334aaf0b17e5"
    }
}
```

**Example 2: 跨应用查询Agent**



Input: 

```
tccli adp DescribeAgentSummaryList --cli-unfold-argument  \
    --Scope 1 \
    --FilterList.0.Name SpaceId \
    --FilterList.0.Operator 0 \
    --FilterList.0.ValueList default_space \
    --PageSize 10 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "AgentList": [
            {
                "AdvancedConfig": {
                    "MaxReasoningRound": 100
                },
                "AgentId": "ecfd551c-43bb-4473-a9e1-dd0b459f38f6",
                "Profile": {
                    "AppName": "待删********用06",
                    "Description": "",
                    "Developer": "co****11",
                    "IconUrl": "https://cdn.xiaowei.qq.com/static/adp/agent-robot.png",
                    "Name": "1***本",
                    "Role": 1
                }
            }
        ],
        "TotalCount": 6,
        "RequestId": "ca855fd9-9db2-482e-bce4-d16a28cf68cf"
    }
}
```

