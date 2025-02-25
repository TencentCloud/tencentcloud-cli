**Example 1: 成功**



Input: 

```
tccli domain CreateInternalComplaint --cli-unfold-argument  \
    --Ctime 2024-11-04 16:50:00 \
    --Name test name \
    --Email test@qq.com \
    --Domain test-domain.xyz \
    --Category test Category \
    --Address test Address \
    --Company test Company \
    --CountryName test CountryName \
    --Describe test Describe \
    --Attachment test Attachment \
    --Url http://Url \
    --InfringedUrl http://InfringedUrl
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-dwdqdw-xxxx"
    }
}
```

