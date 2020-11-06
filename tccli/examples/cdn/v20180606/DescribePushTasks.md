**Example 1: 预热历史查询**



Input: 

```
tccli cdn DescribePushTasks --cli-unfold-argument  \
    --TaskId 1533031853231313311
```

Output: 
```
{
    "Response": {
        "RequestId": "4d5a83f8-a61f-445b-8036-5636be640bef",
        "PushLogs": [
            {
                "TaskId": "1533031853231313311",
                "Url": "http://www.test.com/",
                "Status": "Done",
                "Percent": 100,
                "CreateTime": "2018-07-30 18:10:53",
                "Area": "mainland"
            }
        ],
        "TotalCount": 20
    }
}
```

