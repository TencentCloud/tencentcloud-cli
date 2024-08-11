**Example 1: 更新用户信息**



Input: 

```
tccli smh ModifyUser --cli-unfold-argument  \
    --LibraryId smh08gcw6500e6jl \
    --Filter.Key PhoneNumber \
    --Filter.Value +86-13800000000 \
    --CountryCode +86 \
    --PhoneNumber 13800138000
```

Output: 
```
{
    "Response": {
        "LibraryId": "smh08gcw6500e6jl",
        "UserId": "user18llqxtbrcvgn",
        "CreationTime": "2024-07-07T03:45:26Z",
        "Role": "user",
        "Enabled": true,
        "CountryCode": "+86",
        "PhoneNumber": "13800138000",
        "Email": null,
        "AccountName": null,
        "AccountUserId": null,
        "Comment": "",
        "Nickname": "",
        "Avatar": "",
        "Customize": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

