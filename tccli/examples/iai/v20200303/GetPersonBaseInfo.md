**Example 1: Getting the basic information of person**

This example shows you how to get the information of a specified person, including name, gender, face, etc.

Input: 

```
tccli iai GetPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001
```

Output: 
```
{
    "Response": {
        "PersonName": "EvanLiao",
        "Gender": 1,
        "FaceIds": [
            "2873640802022644880",
            "2875186538564559728"
        ],
        "RequestId": "9568a077-0710-40d2-9d6a-b9483d3f2051"
    }
}
```

**Example 2: Sample error**

The person ID does not exist.

Input: 

```
tccli iai GetPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1002
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonIdNotExist",
            "Message": "The person ID does not exist."
        },
        "RequestId": "98b4a0bc-802b-4764-9701-bc0c6c544395"
    }
}
```

