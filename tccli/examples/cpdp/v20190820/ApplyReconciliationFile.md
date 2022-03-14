**Example 1: ApplyReconciliationFile**



Input: 

```
tccli cpdp ApplyReconciliationFile --cli-unfold-argument  \
    --MidasEnvironment xx \
    --ApplyFileType xx \
    --BankAccountNumber xx \
    --ApplyFileDate xx
```

Output: 
```
{
    "Response": {
        "RequestId": "abb4aa8b-6dfa-47eb-9c4a-de464da32e68",
        "Result": {
            "ApplyFileId": "xx",
            "ApplyStatus": "S",
            "ApplyMessage": "1"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 2: 聚鑫-申请对账文件-成功**



Input: 

```
tccli cpdp ApplyReconciliationFile --cli-unfold-argument  \
    --MidasEnvironment development \
    --ApplyFileType YE \
    --BankAccountNumber 15000101075856 \
    --ApplyFileDate 20220302
```

Output: 
```
{
    "Response": {
        "RequestId": "4de7245d-3c88-4d7d-8116-31e1ec145a16",
        "Result": {
            "ApplyFileId": "20220303181840234585170504588894208",
            "ApplyStatus": "I",
            "ApplyMessage": "申请中"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

