**Example 1: 查询复刻音色**

查询复刻音色

Input: 

```
tccli vrs GetVRSVoiceTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "1234dce8-15d7-abcd-9325-8259266c1234",
        "Data": {
            "VoiceTypeList": [
                {
                    "VoiceType": 111111,
                    "VoiceName": "小红",
                    "VoiceGender": 2,
                    "TaskType": 1,
                    "TaskID": "1234d751-fb5f-4805-889c-2fce9e8babcd",
                    "DateCreated": "2023-10-23T10:25:54+08:00",
                    "IsDeployed": true
                },
                {
                    "VoiceType": 222222,
                    "VoiceName": "小刚",
                    "VoiceGender": 1,
                    "TaskType": 1,
                    "TaskID": "1234ed3d-4026-4e48-9926-382459e4abcd",
                    "DateCreated": "2023-10-20T15:38:28+08:00",
                    "IsDeployed": true
                }
            ]
        }
    }
}
```

