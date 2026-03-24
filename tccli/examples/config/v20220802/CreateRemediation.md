**Example 1: 创建修正设置**



Input: 

```
tccli config CreateRemediation --cli-unfold-argument  \
    --RuleId cr-oPTxveTx0NbmcNmDNoQG \
    --RemediationType SCF \
    --RemediationTemplateId qcs::scf:ap-guangzhou:100000005287:namespace/test/functions/aaa \
    --InvokeType MANUAL_EXECUTION \
    --SourceType CUSTOM
```

Output: 
```
{
    "Response": {
        "RemediationId": "crr-lKj43O4nbSD78XYlvGS9",
        "RequestId": "4c9384a0-e80c-4af0-a84c-8682527c86a0"
    }
}
```

