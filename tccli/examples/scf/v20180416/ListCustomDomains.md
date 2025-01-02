**Example 1: 示例1**



Input: 

```
tccli scf ListCustomDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Domains": [
            {
                "CertConfig": {
                    "CertificateId": "ccccaas"
                },
                "Domain": "www.demo.com",
                "EndpointsConfig": [
                    {
                        "FunctionName": "test1",
                        "Namespace": "default",
                        "PathMatch": "/cc/",
                        "PathRewrite": [
                            {
                                "Path": "/cc/",
                                "Rewrite": "/$1",
                                "Type": "ExactRules"
                            }
                        ],
                        "Qualifier": "$LATEST"
                    }
                ],
                "Protocol": "HTTP&HTTPS",
                "WafConfig": {
                    "WafInstanceId": "",
                    "WafOpen": "CLOSE"
                }
            }
        ],
        "RequestId": "6941ssdd162b-925f-4c3a-b90f-3558c0aebf97",
        "Total": 1
    }
}
```

