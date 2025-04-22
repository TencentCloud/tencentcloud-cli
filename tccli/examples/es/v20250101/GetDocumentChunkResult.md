**Example 1: 获取文档切片结果**



Input: 

```
tccli es GetDocumentChunkResult --cli-unfold-argument  \
    --TaskId 3041d1dc-1072-4025-a3c2-f8baea25801b
```

Output: 
```
{
    "Response": {
        "DocumentChunkResultUrl": "https://aisearch-xxx.cos.ap-guangzhou.myqcloud.com/%2F1257780094/2032/0eef71d5c6b94f4c9f77bf96a990dd93.zip?x-cos-security-token=dOBUL5WAbHvrSLvR7Gw6r8quYTekAtja3bbc5bdae040e3fb733c657573859b48kjO-Uu0jMRpnX4JBXiMCmDLWHD-hkBEcwXSrKEkAfuV5Gb8r2Gx4yUlNGzpEgZpn13dTyMMyYUGmaeteIWndTZrLijqaUwuh-PiPfNFi7s2a3Cc_L-pAmY0LMpvMun98jP5Z26nrJ2XDgg9mN1oXTWz-BRohOXFe6Yo1sBzLdjIBMti4hfycleXOOmP2eVl5qbtd_dKog0NFfkPOot3kCRSVA5SIws5gS57oyhukNQTepOjvvf31qj0jxSPd0N2ipJWROLC3xcf31PSK8oBeefi4a0byIIMpauiuzqL81TFQ82mzut8lROA23aIEyrcHfAH33La3IK4i24edP-f58UTwyrBwsmsX1TIxvhQzgKA&q-sign-algorithm=sha1&q-ak=AKIDKI_3jDhy9q_C7NWV-fcXj0Ra0-ii9R1_cn7MHDdtqwIizIrVqVNUQDSsnYbirlgA&q-sign-time=1744101492%3B1744187892&q-key-time=1744101492%3B1744187892&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=3edbadc81bcdbe994ba75e9d578a3b2ffaf551ca",
        "RequestId": "0b2bf3af-5671-45e8-a5db-b6792a928aa6",
        "Status": 1,
        "Usage": {
            "PageNumber": 1,
            "TotalTokens": 118
        }
    }
}
```

