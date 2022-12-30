**Example 1: 获取采集器列表**



Input: 

```
tccli wedata DescribeInLongAgentList --cli-unfold-argument  \
    --Status xx \
    --PageIndex 1 \
    --VpcId xx \
    --PageSize 1 \
    --ProjectId xx \
    --AgentType 1 \
    --AgentName xx \
    --AgentId xx
```

Output: 
```
{
    "Response": {
        "PageIndex": 1,
        "PageSize": 1,
        "Items": [
            {
                "Status": "xx",
                "AgentTotal": 1,
                "VpcId": "xx",
                "ExecutorGroupId": "xx",
                "AgentType": 1,
                "AgentGroupId": "xx",
                "StatusDesc": "xx",
                "Source": "xx",
                "ExecutorGroupName": "xx",
                "TaskCount": 1,
                "AgentName": "xx",
                "AgentId": "xx",
                "CvmAgentStatusList": [
                    {
                        "Status": "xx",
                        "Count": 1
                    }
                ]
            }
        ],
        "TotalPage": 1,
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

