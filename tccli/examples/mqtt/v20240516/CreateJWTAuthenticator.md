**Example 1: 示例**

示例

Input: 

```
tccli mqtt CreateJWTAuthenticator --cli-unfold-argument  \
    --InstanceId mqtt-jeredv33 \
    --Algorithm hmac-based \
    --From username \
    --Secret 123 \
    --Status open
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "1c0dfde9-086d-49b5-a49d-8de4e30c66ad"
    }
}
```

