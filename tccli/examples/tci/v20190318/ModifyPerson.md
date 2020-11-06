**Example 1: 修改人员详情**

修改人员详情

Input: 

```
tccli tci ModifyPerson --cli-unfold-argument  \
    --PersonName xxx \
    --PersonId personid_xxx \
    --LibraryId library_xxx \
    --PhoneNumber xxx \
    --StudentNumber xxx \
    --JobNumber xxx \
    --Male 1 \
    --Mail xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3903c090-485c-433f-9570-cf52f0ea04ba",
        "PersonName": "xxx",
        "PersonId": "person_xxx",
        "LibraryId": "library_xxx"
    }
}
```

