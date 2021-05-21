**Example 1: 删除域名**



Input: 

```
tccli dnspod DeleteDomain --cli-unfold-argument  \
    --Domain dnspod.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

**Example 2: DeleteDomain_success**



Input: 

```
tccli dnspod DeleteDomain --cli-unfold-argument  \
    --Domain iceice.club
```

Output: 
```
{
    "Response": {
        "RequestId": "5d459ba8-f335-4508-b6b2-efed8b531c8c"
    }
}
```

