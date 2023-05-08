**Example 1: 获取采集器列表**

获取采集器列表

Input: 

```
tccli wedata DescribeInLongAgentList --cli-unfold-argument  \
    --AgentId abc \
    --AgentName abc \
    --AgentType 1 \
    --Status abc \
    --VpcId abc \
    --PageIndex 1 \
    --PageSize 1 \
    --ProjectId abc \
    --Like 1 \
    --AgentTypes abc
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AgentId": "abc",
                "AgentName": "abc",
                "Status": "abc",
                "StatusDesc": "abc",
                "AgentType": 1,
                "Source": "abc",
                "VpcId": "abc",
                "ExecutorGroupId": "abc",
                "ExecutorGroupName": "abc",
                "TaskCount": 1,
                "AgentGroupId": "abc",
                "CvmAgentStatusList": [
                    {
                        "Status": "abc",
                        "Count": 1
                    }
                ],
                "AgentTotal": 1,
                "LifeDays": 0
            }
        ],
        "PageIndex": 1,
        "PageSize": 1,
        "TotalCount": 1,
        "TotalPage": 1,
        "RequestId": "abc"
    }
}
```

