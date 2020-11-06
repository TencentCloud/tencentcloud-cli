**Example 1: 创建人员**

创建人员

Input: 

```
tccli tci CreatePerson --cli-unfold-argument  \
    --PersonName xxx \
    --LibraryId library_id \
    --PhoneNumber xxx \
    --StudentNumber xxxx \
    --JobNumber xxx \
    --Male 1 \
    --Mail xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "366c1cc8-30fe-4c24-a3ac-85fa3459a88c",
        "PersonName": "xxx",
        "PersonId": "person_1553000279384479226589",
        "LibraryId": "library_1552907886376820469"
    }
}
```

