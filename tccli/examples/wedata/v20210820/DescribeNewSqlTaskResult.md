**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeNewSqlTaskResult --cli-unfold-argument  \
    --DetailId 123
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "InstanceId": "20220218112409315_2022-03-02T17:07:37+08:00",
        "RecordId": 123,
        "DetailId": 123,
        "ResultSet": true,
        "ResultContent": "select 1",
        "FieldList": [
            "123"
        ]
    }
}
```

