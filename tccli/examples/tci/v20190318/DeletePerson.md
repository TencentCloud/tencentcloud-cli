**Example 1: 删除人员**

删除人员

Input: 

```
tccli tci DeletePerson --cli-unfold-argument  \
    --PersonId person_xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b8d386f8-50d6-44c6-a497-4c5783d91473",
        "PersonName": "xxx",
        "PersonId": "person_xxx",
        "LibraryId": "library_xxx"
    }
}
```

