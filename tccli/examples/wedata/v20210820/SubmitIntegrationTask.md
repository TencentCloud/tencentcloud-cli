**Example 1: 案例1**



Input: 

```
tccli wedata SubmitIntegrationTask --cli-unfold-argument  \
    --GroupId asdf \
    --ResourceId asdfasdf \
    --ResourceRegion adfasdf \
    --RemotePath adsfadsf \
    --ProjectId ddddd \
    --ResourceBucket dddd \
    --RunParams {"name":"tom"}
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "Record": {
            "Id": 858,
            "InstanceId": "20220218112409315_2022-03-02T17:07:37+08:00",
            "ScriptContent": "select name from student where name='ccc';",
            "CreateTime": "2022-03-02T17:07:36+08:00",
            "Status": null
        },
        "Details": [
            {
                "Id": 858,
                "ScriptContent": "select name from student where name='ccc';",
                "StartTime": "2022-03-02T17:07:36+08:00",
                "EndTime": "2022-03-02T17:07:36+08:00",
                "Status": "CREATED",
                "RecordId": 858
            }
        ]
    }
}
```

