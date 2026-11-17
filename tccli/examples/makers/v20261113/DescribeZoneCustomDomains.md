**Example 1: 查询自定义域名**



Input: 

```
tccli makers DescribeZoneCustomDomains --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************
```

Output: 
```
{
    "Response": {
        "PagesDomains": [
            {
                "Area": "overseas",
                "Cname": null,
                "Domain": "************************",
                "Env": "Production",
                "ForceRedirect": {
                    "RedirectStatusCode": 302,
                    "Switch": "off"
                },
                "Hsts": {
                    "IncludeSubDomains": "off",
                    "MaxAge": 0,
                    "Preload": "off",
                    "Switch": "off"
                },
                "Http2": {
                    "Switch": "off"
                },
                "Ipv6": {
                    "Switch": "off"
                },
                "MainDomain": "*********",
                "OcspStapling": {
                    "Switch": "off"
                },
                "OwnershipVerification": {
                    "DnsVerification": {
                        "RecordType": "TXT",
                        "RecordValue": "reclaim-********************************",
                        "Subdomain": "*****************************"
                    },
                    "FileVerification": {
                        "Content": "********************************",
                        "Path": "********************************************"
                    },
                    "NsVerification": null
                },
                "Status": "init",
                "Type": "Custom",
                "ZoneId": "zone-************"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ef221935-2ac7-4f9c-acbb-d28e7e7a85e3"
    }
}
```

