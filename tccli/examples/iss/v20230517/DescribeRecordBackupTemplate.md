**Example 1: 成功**

 

Input: 

```
tccli iss DescribeRecordBackupTemplate --cli-unfold-argument  \
    --TemplateId abcdefgh-1234-5678-ijkl-1234567890ab
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateAt": "2023-06-02 18:35:35",
            "DevTimeSections": [
                {
                    "DayOfWeek": 1,
                    "EndTime": "00:23:00",
                    "StartTime": "00:00:00"
                }
            ],
            "Scale": 1,
            "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
            "TemplateName": "test1",
            "TimeSections": [
                {
                    "DayOfWeek": 2,
                    "EndTime": "00:30:00",
                    "StartTime": "00:00:00"
                }
            ],
            "UpdateAt": "2023-06-02 19:53:22"
        },
        "RequestId": "d52b43e5-28da-45b8-878b-f94d89dbf5a5"
    }
}
```

