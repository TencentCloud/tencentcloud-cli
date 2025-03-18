**Example 1: 示例**

示例

Input: 

```
tccli mqtt RegisterDeviceCertificate --cli-unfold-argument  \
    --InstanceId mqtt-jbgwp4ae \
    --DeviceCertificate -----BEGIN CERTIFICATE-----
ajvuaaIlJp7GgOZxxPInOVXPmBlBlp28AiMlmxSfSAuMpUF0I8w=
-----END CERTIFICATE-----
 \
    --CaSn 1b1e3bf3702110125887a3a721a7e66f05522513 \
    --ClientId VIN0001
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "49af88f0-6571-4aa4-af92-9261f28c0ed9"
    }
}
```

