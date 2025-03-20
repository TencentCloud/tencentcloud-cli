**Example 1: 查询安全日志接入列表**

查询安全日志接入列表

Input: 

```
tccli tcss DescribeSecLogJoinTypeList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Count": 1931,
                "SuperNodeCount": 21,
                "IsJoined": true,
                "LogType": "container_bash"
            }
        ],
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

