**Example 1: 签约行为上报**

用于平台签约行为上报场景。

Input: 

```
tccli cpdp RegisterBehavior --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SignChannel 1 \
    --MacAddress A1:B1:C1:D1:E1:F1 \
    --OperationClickTime 20210513120030 \
    --MidasSignature your_midas_signature \
    --MidasSecretId your_midas_secret_id \
    --FunctionFlag 1 \
    --SubAppId your_sub_app_id \
    --IpAddress 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RegisterInfo": null,
        "ReplenishSuccessFlag": null,
        "RequestId": "4899ec78-5374-4ab4-bc0c-d758126c77b1"
    }
}
```

