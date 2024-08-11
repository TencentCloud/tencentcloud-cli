**Example 1: 新建用户**



Input: 

```
tccli smh CreateUser --cli-unfold-argument  \
    --LibraryId smh08gcw6500e6jl \
    --Role user \
    --Enabled True
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
        "CountryCode": null,
        "PhoneNumber": null,
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

