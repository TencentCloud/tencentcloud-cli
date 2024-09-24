**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeAuthenticator --cli-unfold-argument  \
    --InstanceId mqtt-2vnk55xv \
    --Type JWKS
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Authenticators": [
            {
                "Config": "{\"endpoint\":\"1.2.3.4\",\"refreshInterval\":10}",
                "Status": "open",
                "Type": "JWKS"
            }
        ],
        "RequestId": "83d4a381-b448-45c8-adcf-b563bd18f4fb"
    }
}
```

