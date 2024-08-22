**Example 1: DescribeUser**



Input: 

```
tccli tcmpp DescribeUser --cli-unfold-argument  \
    --UserId U20240819174742HGXHXT \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "UserId": "U20240819174742HGXHXT",
            "UserAccount": "OpenApiUser0819174740",
            "UserName": "OpenApiUser0819174740",
            "AccountType": 3
        },
        "RequestId": "1de585c1-8d2a-46ec-bcd4-f2e2a3bc9f5b"
    }
}
```

