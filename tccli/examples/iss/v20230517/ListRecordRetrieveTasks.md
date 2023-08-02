**Example 1: 不存在取回任务**

 

Input: 

```
tccli iss ListRecordRetrieveTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 存在取回任务**

 

Input: 

```
tccli iss ListRecordRetrieveTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "9ee325e9984**********a805c19b4e1",
                "TaskName": "name",
                "Describe": "",
                "StartTime": 1658973728,
                "EndTime": 1658973828,
                "ChannelCount": 1,
                "Mode": 1,
                "Expiration": 10,
                "Status": 1,
                "Capacity": 64
            },
            {
                "TaskId": "48676e89a8c**********baa36220fa4",
                "TaskName": "name",
                "Describe": "",
                "StartTime": 1658973728,
                "EndTime": 1658973828,
                "ChannelCount": 1,
                "Mode": 1,
                "Expiration": 10,
                "Status": 1,
                "Capacity": 64
            }
        ],
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

