**Example 1: NFC比对**



Input: 

```
tccli faceid GetNFCResult --cli-unfold-argument  \
    --NFCToken a1cfec70-4b29-11f0-bce7-c66e37472b33 \
    --IdNum 111111111111111111 \
    --Name 韦小宝 \
    --EnName  \
    --Picture base64 \
    --BirthDate 19460815 \
    --Address 北京市xxxx \
    --Nation 汉 \
    --Sex 男 \
    --SigningOrganization  \
    --BeginTime  \
    --EndTime  \
    --CountryCode  \
    --Nationality  \
    --MachineReadCode 343dasd
```

Output: 
```
{
    "Response": {
        "IdType": "0",
        "CheckMRTD": "0",
        "IdNumCompareResult": "0",
        "NameCompareResult": "0",
        "PictureCompareSim": 85.5,
        "BirthDateCompareResult": "0",
        "BeginTimeCompareResult": "0",
        "EndTimeCompareResult": "0",
        "AddressCompareResult": "0",
        "NationCompareResult": "0",
        "SexCompareResult": "0",
        "EnNameCompareResult": "0",
        "SigningOrganizationCompareResult": "0",
        "NationalityCompareResult": "0",
        "CountryCodeCompareResult": "0",
        "MachineReadCodeCompareResult": "0",
        "PictureCompareResult": "0",
        "ChargeCode": "0",
        "RequestId": "fb2675fb-40e6-42ce-a958-d72413197ad1"
    }
}
```

