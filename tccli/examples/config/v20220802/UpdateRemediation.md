**Example 1: 编辑修正设置**



Input: 

```
tccli config UpdateRemediation --cli-unfold-argument  \
    --RemediationId crr-Z80LHNfW09bakPGFd9cj \
    --RemediationType SCF \
    --RemediationTemplateId qcs::scf:ap-guangzhou:100000005287:namespace/test/functions/bbb \
    --InvokeType MANUAL_EXECUTION \
    --SourceType CUSTOM
```

Output: 
```
{
    "Response": {
        "RequestId": "9d52941a-5658-4dd3-b08c-590071eee6a7"
    }
}
```

