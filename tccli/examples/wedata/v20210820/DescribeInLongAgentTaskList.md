**Example 1: DescribeInLongAgentTaskList**



Input: 

```
tccli wedata DescribeInLongAgentTaskList --cli-unfold-argument  \
    --ProjectId abc \
    --AgentId abc
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "TaskName": "abc",
                "TaskId": "abc",
                "TaskStatus": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

