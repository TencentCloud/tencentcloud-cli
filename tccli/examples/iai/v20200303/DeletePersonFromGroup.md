**Example 1: Deleting person from group**

This example shows you how to remove a person from a specified group. This operation only affects the group.

Input: 

```
tccli iai DeletePersonFromGroup --cli-unfold-argument  \
    --PersonId 1001 \
    --GroupId TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "RequestId": "f9b22bbc-c94d-4287-a2ab-fa68f7bbbaf3"
    }
}
```

**Example 2: Sample error**

The specified person is not in the group.

Input: 

```
tccli iai DeletePersonFromGroup --cli-unfold-argument  \
    --PersonId 3001 \
    --GroupId ZhuYuanDormitoryNo1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.GroupPersonMapNotExist",
            "Message": "The ID of the corresponding person is not in the group."
        },
        "RequestId": "b9d9641d-3de2-4a6f-a728-36a3b66e7bd0"
    }
}
```

