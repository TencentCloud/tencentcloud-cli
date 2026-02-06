**Example 1: 成功调用**



Input: 

```
tccli wedata GetDataSourceRelatedTasks --cli-unfold-argument  \
    --Id 61964
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ProjectId": "1486804694126882816",
                "ProjectName": "u6570u636eu96c6u6210_u8054u8c03",
                "TaskInfo": [
                    {
                        "TaskList": null,
                        "TaskNum": 1,
                        "TaskType": "hybris"
                    }
                ]
            }
        ],
        "RequestId": "a83b5101-89bb-4a83-8181-7353f1e506d7"
    }
}
```

