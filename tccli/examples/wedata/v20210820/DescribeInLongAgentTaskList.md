**Example 1: DescribeInLongAgentTaskList**



Input: 

```
tccli wedata DescribeInLongAgentTaskList --cli-unfold-argument  \
    --ProjectId xx \
    --AgentId xx
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "TaskName": "xx",
                "TaskId": "xx",
                "TaskStatus": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

