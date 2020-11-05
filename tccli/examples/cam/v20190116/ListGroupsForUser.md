**Example 1: Getting the List of User Groups Associated with a User**



Input: 

```
tccli cam ListGroupsForUser --cli-unfold-argument  \
    --Uid 1001408
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "GroupInfo": [
            {
                "GroupId": 2020,
                "GroupName": "test1",
                "CreateTime": "2019-04-03 15:11:34",
                "Remark": "test2"
            }
        ],
        "RequestId": "a614c392-3079-4dab-b819-0ab0563a32f0"
    }
}
```

