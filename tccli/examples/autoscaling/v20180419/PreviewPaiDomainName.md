**Example 1: Previewing a public address instance domain name**

This example shows you how to query domain name that can be used to create a public address instance.

Input: 

```
tccli as PreviewPaiDomainName --cli-unfold-argument  \
    --DomainNameType tcb
```

Output: 
```
{
    "Response": {
        "DomainName": "salmonberry-ey5t3l0k.pai.tcloudbase.com",
        "RequestId": "cea75193-a9fb-4811-aa0b-b4d2096ef0d9"
    }
}
```

