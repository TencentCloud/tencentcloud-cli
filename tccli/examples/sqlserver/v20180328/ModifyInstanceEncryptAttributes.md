**Example 1: 开通实例的TDE加密功能**

开通实例的TDE加密功能

Input: 

```
tccli sqlserver ModifyInstanceEncryptAttributes --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --CertificateAttribution self \
    --QuoteUin 
```

Output: 
```
{
    "Response": {
        "FlowId": 12098283,
        "RequestId": "5062de55-d048-4d3b-92f9-b98b6f244360"
    }
}
```

