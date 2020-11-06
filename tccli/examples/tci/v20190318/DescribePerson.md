**Example 1: 获取人员详细信息**

获取人员详细信息

Input: 

```
tccli tci DescribePerson --cli-unfold-argument  \
    --PersonId person_xxx \
    --LibraryId xxx
```

Output: 
```
{
    "Response": {
        "PersonId": "person_xxx",
        "PersonName": "xxx",
        "LibraryId": "library_xxx",
        "PhoneNumber": "xxx",
        "StudentNumber": "xxx",
        "JobNumber": "xxx",
        "Male": 1,
        "Mail": "xxx",
        "CreateTime": "2019-03-19T20:57:59+08:00",
        "UpdateTime": "2019-03-19T21:08:40+08:00",
        "FaceSet": null,
        "RequestId": "735881d4-91cf-46c4-9283-f232bdb67b71"
    }
}
```

