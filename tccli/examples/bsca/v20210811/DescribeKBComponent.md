**Example 1: 查询openssl组件信息**



Input: 

```
tccli bsca DescribeKBComponent --cli-unfold-argument  \
    --PURL.Name openssl
```

Output: 
```
{
    "Response": {
        "Component": {
            "CodeLocationList": null,
            "Homepage": "https://www.openssl.org",
            "LicenseExpression": "openssl-ssleay",
            "NicknameList": null,
            "PURL": {
                "Name": "openssl",
                "Namespace": "",
                "Protocol": "generic",
                "Qualifiers": null,
                "Subpath": "",
                "Version": ""
            },
            "Summary": "OpenSSL is a toolkit for supporting cryptography. The openssl-static\npackage contains static libraries needed for static linking of\napplications which support various cryptographic algorithms and\nprotocols."
        },
        "RequestId": "56dabf5e-0887-4960-bf6f-595ea9a9a0d7"
    }
}
```

