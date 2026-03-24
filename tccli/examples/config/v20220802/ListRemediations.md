**Example 1: 查询修正列表**



Input: 

```
tccli config ListRemediations --cli-unfold-argument  \
    --Limit 10 \
    --RuleIds cr-hZWheBkQnPHGoRDUPd0N
```

Output: 
```
{
    "Response": {
        "Remediations": [
            {
                "InvokeType": "NON_EXECUTION",
                "OwnerUin": "100000005287",
                "RemediationId": "crr-PYS0P5YUE1R1gavTDxlU",
                "RemediationSourceType": "SCF",
                "RemediationTemplateId": "qcs::scf:ap-guangzhou:100000005287:namespace/test/functions/aaa",
                "RemediationType": "SCF",
                "RuleId": "cr-hZWheBkQnPHGoRDUPd0N"
            }
        ],
        "Total": 1,
        "RequestId": "1002ea5c-ce56-4a2e-9cab-ffd5016a11a1"
    }
}
```

