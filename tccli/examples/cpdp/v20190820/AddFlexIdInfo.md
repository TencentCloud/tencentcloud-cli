**Example 1: 补充用户证件信息**



Input: 

```
tccli cpdp AddFlexIdInfo --cli-unfold-argument  \
    --PayeeId 1529657731805986816 \
    --IdType 0 \
    --IdNo xxxxxxx
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": null,
        "RequestId": "8ffecac1-2d89-43a9-9075-a985442ef466"
    }
}
```

