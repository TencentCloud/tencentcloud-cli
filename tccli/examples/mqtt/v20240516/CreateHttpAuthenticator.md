**Example 1: 示例**

示例

Input: 

```
tccli mqtt CreateHttpAuthenticator --cli-unfold-argument  \
    --InstanceId mqtt-3ogawe7n \
    --Endpoint 127.0.0.1 \
    --Status open \
    --Header.0.Key user \
    --Header.0.Value ${username} \
    --Body.0.Key user \
    --Body.0.Value ${username}
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "6f36142e-0e1a-4540-ba32-2b1d223672c6"
    }
}
```

