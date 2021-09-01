**Example 1: ApplyOutwardOrder**



Input: 

```
tccli cpdp ApplyOutwardOrder --cli-unfold-argument  \
    --TransactionId trasid201911230012 \
    --PricingCurrency CNY \
    --SourceCurrency CNY \
    --SourceAmount 10 \
    --TargetCurrency USD \
    --PayeeType BANK_ACCOUNT \
    --PayeeAccount 325119780000 \
    --PayeeName TEST \
    --PayeeAddress TEST \
    --PayeeBankAccountType CORPORATE \
    --PayeeCountryCode USA \
    --PayeeBankName TEST \
    --PayeeBankAddress TEST \
    --PayeeBankDistrict US \
    --PayeeBankSwiftCode CITIUS33XXX \
    --PayeeBankCode 026009593 \
    --ReferenceForBeneficiary test
```

Output: 
```
{
    "Response": {
        "RequestId": "81687630-ec4c-4325-9946-ab1054c07a80",
        "Result": {
            "Data": {
                "Status": "WAIT_PAYMENT",
                "MerchantId": "202002270000054004",
                "TransactionId": "trasid201911230012"
            },
            "Code": "000000"
        }
    }
}
```

