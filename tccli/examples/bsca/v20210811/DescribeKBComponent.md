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
            "CodeLocationList": [
                "https://github.com/openssl/openssl.git",
                "https://android.googlesource.com/platform/external/openssl"
            ],
            "Homepage": "https://www.openssl.org",
            "LastUpdateTime": "2023-09-11 22:08:48.000000",
            "LicenseExpression": "openssl-ssleay",
            "NicknameList": null,
            "PURL": {
                "Name": "openssl",
                "Namespace": "",
                "Protocol": "generic",
                "Qualifiers": [],
                "Subpath": "",
                "Version": "1.0.0"
            },
            "Summary": "OpenSSL is a robust, commercial-grade, full-featured Open Source Toolkit for the Transport Layer Security (TLS) protocol formerly known as the Secure Sockets Layer (SSL) protocol. The protocol implementation is based on a full-strength general purpose cryptographic library, which can also be used stand-alone.",
            "TagList": [
                "network"
            ],
            "VersionInfo": {
                "CopyrightList": [
                    "Copyright (c) 1998-2008 The OpenSSL Project",
                    "Copyright (c) 1995-1998 Eric Young (eay@cryptsoft.com)",
                    "holder is Tim Hudson (tjh@cryptsoft.com)"
                ],
                "PublishTime": "2015-01-22 09:46:52.000000",
                "TagList": [
                    "copyright_updated"
                ]
            }
        },
        "RequestId": "deadc0de-3ab7-45dd-9def-6b3e087dd354"
    }
}
```

