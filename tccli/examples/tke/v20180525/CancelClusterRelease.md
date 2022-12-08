**Example 1: 取消集群应用**



Input: 

```
tccli tke CancelClusterRelease --cli-unfold-argument  \
    --ID 0b49c73e-a2eb-41d7-8a9b-c0e61cf1aabb
```

Output: 
```
{
    "Response": {
        "Release": {
            "Condition": "",
            "CreatedTime": "2020-04-15T14:44:42Z",
            "ID": "0b49c73e-a2eb-41d7-8a9b-c0e61cf1aabb",
            "Name": "app-04",
            "Namespace": "lwj",
            "Status": "failed",
            "UpdatedTime": "2020-04-15T14:44:43Z"
        },
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

