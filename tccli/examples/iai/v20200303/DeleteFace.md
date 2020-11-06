**Example 1: Deleting face**

This example shows you how to delete the face images of a person.

Input: 

```
tccli iai DeleteFace --cli-unfold-argument  \
    --PersonId 1001 \
    --FaceIds 2875186538564559728
```

Output: 
```
{
    "Response": {
        "SucDeletedNum": 1,
        "SucFaceIds": [
            "2875186538564559728"
        ],
        "RequestId": "38f96439-d5ea-48ea-899b-44a284708f6b"
    }
}
```

**Example 2: Sample error**

The person ID does not exist.

Input: 

```
tccli iai DeleteFace --cli-unfold-argument  \
    --PersonId 5001 \
    --FaceIds 2875186538564559728
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ErrorPersonNotExisted",
            "Message": "The person does not exist."
        },
        "RequestId": "e2b603e5-51d0-4a8a-8319-2df026ae7518"
    }
}
```

