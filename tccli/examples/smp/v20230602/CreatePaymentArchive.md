**Example 1: 入参**



Input: 

```
tccli smp CreatePaymentArchive --cli-unfold-argument  \
    --PaymentTraceId 5ce2d8d5-5173-47a0-895d-4c0052d97f5f \
    --RealPayAmountTotal 100.14 \
    --ApprovalNumber abc123
```

Output: 
```
{
    "Response": {
        "RequestId": "cad3a73d-ff17-4176-9f8e-7087ccdeb460",
        "Data": {
            "Code": 0,
            "Message": ""
        }
    }
}
```

