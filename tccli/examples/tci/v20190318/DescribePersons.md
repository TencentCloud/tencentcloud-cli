**Example 1: 拉取指定库人员列表**

拉取指定库人员列表

Input: 

```
tccli tci DescribePersons --cli-unfold-argument  \
    --LibraryId libraryid_xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "0a28dd6b-138a-4c6c-8ce3-d1e1bb6954d4",
        "TotalCount": 1,
        "PersonSet": [
            {
                "PersonId": "person_xxx",
                "PersonName": "xxx",
                "LibraryId": "library_xxx",
                "PhoneNumber": "xxx",
                "StudentNumber": "xxx",
                "JobNumber": "xxx",
                "Male": 1,
                "Mail": "xxx",
                "CreateTime": "2019-03-19T20:57:59+08:00",
                "UpdateTime": "2019-03-19T21:08:40+08:00"
            }
        ]
    }
}
```

