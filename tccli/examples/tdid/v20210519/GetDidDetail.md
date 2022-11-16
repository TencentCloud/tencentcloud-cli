**Example 1: GetDidInfo**

DID详情

Input: 

```
tccli tdid GetDidDetail --cli-unfold-argument  \
    --Did xx
```

Output: 
```
{
    "Response": {
        "Did": "did:weid:1:0xc89a0423e25bea56c9f3c33098a41b100795946b",
        "Remark": "",
        "PublicKey": "6584791555786563316509885238222269581668944990935472251441138953175584477704980511086954755594925031757290408838181535373243875909851103030607080357950575",
        "AuthorityState": 0,
        "ConsortiumId": 617,
        "ConsortiumName": "bigbang",
        "GroupId": 1,
        "ClusterId": "bcos-fmtkyt8xne",
        "ResChainId": "1tbaas-k0j8i7lqc4",
        "CreateTime": "2021-06-29 16:27:26",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

