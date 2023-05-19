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
                "LogType": "container_bash",
                "Count": 10,
                "IsJoined": true
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

