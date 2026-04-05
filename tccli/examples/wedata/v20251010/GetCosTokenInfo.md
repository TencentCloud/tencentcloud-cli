**Example 1: 获取costoken**

获取costoken

Input: 

```
tccli wedata GetCosTokenInfo --cli-unfold-argument  \
    --WorkspaceId sdf \
    --RoomKey sdfs
```

Output: 
```
{
    "Response": {
        "Data": {
            "ExpiredTime": "0",
            "SecretId": "",
            "SecretKey": "",
            "StartTime": "0",
            "Token": ""
        },
        "RequestId": "a609f447-a10e-45fc-9bd9-8c339dfe9b1e"
    }
}
```

