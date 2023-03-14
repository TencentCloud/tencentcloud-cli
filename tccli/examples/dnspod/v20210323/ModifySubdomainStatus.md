**Example 1: 暂停@子域名A和TXT类型的解析记录**

 暂停@子域名A和TXT类型的解析记录

Input: 

```
tccli dnspod ModifySubdomainStatus --cli-unfold-argument  \
    --Domain dnspod.site \
    --RecordType A,TXT \
    --Status disable
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

**Example 2: 暂停www子域名A/TXT/CNAME类型的解析记录**

 暂停www子域名A/TXT/CNAME类型的解析记录

Input: 

```
tccli dnspod ModifySubdomainStatus --cli-unfold-argument  \
    --Domain dnspod.site \
    --SubDomain test \
    --RecordType A,TXT,CNAME \
    --Status disable
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

