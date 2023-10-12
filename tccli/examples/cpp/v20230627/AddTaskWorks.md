**Example 1: AddTaskWorks**



Input: 

```
tccli cpp AddTaskWorks --cli-unfold-argument  \
    --Works.0.WorksName abc \
    --Works.0.PublishTime abc \
    --Works.0.MediaType 0 \
    --Works.0.WorksAuthor abc \
    --Works.0.Url abc \
    --Works.0.WorksTag abc \
    --Works.0.WorksType abc \
    --Works.0.ExtraInfo.Description abc \
    --Works.0.TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "WorkId": "abc",
                "WorkName": "abc",
                "Url": "abc",
                "TaskId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

