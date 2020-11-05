**Example 1: Calling the DeleteGroup API**

This example shows you how to delete a specified group and all its members.

Input: 

```
tccli iai DeleteGroup --cli-unfold-argument  \
    --GroupId ZhuYuanDormitoryNo1
```

Output: 
```
{
    "Response": {
        "RequestId": "2ff7181c-ef20-4f02-b4ed-13924b381368"
    }
}
```

**Example 2: Sample Error**

This example shows the error occurred when the specified group ID does not exist.

Input: 

```
tccli iai DeleteGroup --cli-unfold-argument  \
    --GroupId ZhuYuanDormitory
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "The specified group ID does not exist."
        },
        "RequestId": "878b225f-d3a4-4aa0-a849-3df415ac61a9"
    }
}
```

