**Example 1: 查询镜像关联主机**



Input: 

```
tccli tcss DescribeAssetImageHostList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ImageID": "sha256:bd571e6529f32461648680c82e2540f9db4b3bb********",
                "HostID": "5cd1c13e-d18a-4904-ada3-a2********"
            },
            {
                "ImageID": "sha256:d6e46aa2470df1d32034c6707c8041158b6********",
                "HostID": "5cd1c13e-d18a-4904-ada3-a2ef********"
            }
        ],
        "RequestId": "f28e2b9b-ee35-4c82-87e4-fcb64671d2af",
        "TotalCount": 24
    }
}
```

