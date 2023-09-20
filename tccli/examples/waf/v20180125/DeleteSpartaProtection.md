**Example 1: Saas型WAF删除防护域名**



Input: 

```
tccli waf DeleteSpartaProtection --cli-unfold-argument  \
    --Edition sparta-waf \
    --Domains www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "afa27f36-13f0-4c2c-b36b-bc70e79b4896"
    }
}
```

