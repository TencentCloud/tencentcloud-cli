**Example 1: 成功**

 

Input: 

```
tccli iss DeleteUserDevice --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "21367370-7efc-4c0c-b321-9bb3dd66ce60"
    }
}
```

**Example 2: 设备不存在**

 

Input: 

```
tccli iss DeleteUserDevice --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "该资源不存在"
        },
        "RequestId": "8f530b9c-dae9-49e7-b30a-403c9a9a2437"
    }
}
```

