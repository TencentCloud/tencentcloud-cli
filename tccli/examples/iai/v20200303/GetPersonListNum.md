**Example 1: Calling the GetPersonListNum API**

This example shows you how to get the number of persons in the specified group.

Input: 

```
tccli iai GetPersonListNum --cli-unfold-argument  \
    --GroupId TencentShenZhenEmployee
```

Output: 
```
{
    "Response": {
        "PersonNum": 2,
        "FaceNum": 2,
        "RequestId": "18fb1e31-0d33-4371-9f41-b1fd59e0c781"
    }
}
```

**Example 2: Sample Error**

This example shows the error occurred when the specified group ID does not exist.

Input: 

```
tccli iai GetPersonListNum --cli-unfold-argument  \
    --GroupId Tencent
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "The specified group ID does not exist."
        },
        "RequestId": "2865a458-4db1-46bd-ae52-b7507c9f4e62"
    }
}
```

