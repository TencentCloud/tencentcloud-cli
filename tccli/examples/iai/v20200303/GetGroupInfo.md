**Example 1: Getting group information**



Input: 

```
tccli iai GetGroupInfo --cli-unfold-argument  \
    --GroupId aaa
```

Output: 
```
{
    "Response": {
        "GroupName": "aaa",
        "GroupId": "aaa",
        "GroupExDescriptions": [
            "24"
        ],
        "Tag": "fdsaf",
        "FaceModelVersion": "3.0",
        "CreationTimestamp": 1559530931613,
        "RequestId": "6faa05d0-287b-464e-8755-cf3e8d0c703d"
    }
}
```

