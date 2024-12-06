**Example 1: 示例**

示例

Input: 

```
tccli mqtt ModifyJWTAuthenticator --cli-unfold-argument  \
    --InstanceId mqtt-mmgej724 \
    --Algorithm hmac-based \
    --From username \
    --Secret secret1 \
    --Remark remark1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "1440f718-1578-494b-aab0-8fe0bf7095cd"
    }
}
```

