**Example 1: Deleting person**

This example shows you how to delete the information of a specified person.

Input: 

```
tccli iai DeletePerson --cli-unfold-argument  \
    --PersonId 2001
```

Output: 
```
{
    "Response": {
        "RequestId": "4b609b7c-7a9a-4ea0-be8b-1fb638c2ceca"
    }
}
```

**Example 2: Sample error**

The person ID does not exist.

Input: 

```
tccli iai DeletePerson --cli-unfold-argument  \
    --PersonId 3001
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ErrorPersonNotExisted",
            "Message": "The person does not exist."
        },
        "RequestId": "4b9c1bdc-86eb-413f-8c74-15bcf4466cd5"
    }
}
```

