**Example 1: 域名过户**

域名转移给其他腾讯云账户

Input: 

```
tccli domain ModifyDomainOwner --cli-unfold-argument  \
    --DomainId 域名ID \
    --NewOwnerUin 新用户UIN
```

Output: 
```
{
    "Response": {
        "TransferDnsResult": null,
        "RequestId": "abcd-abcd-abcd-abcd"
    }
}
```

