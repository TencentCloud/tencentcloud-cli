**Example 1: 查询 apache-2.0 许可证信息**



Input: 

```
tccli bsca DescribeKBLicense --cli-unfold-argument  \
    --LicenseExpression apache-2.0
```

Output: 
```
{
    "Response": {
        "LicenseList": [
            {
                "LicenseDetail": {
                    "ConditionSet": [
                        {
                            "Description": "A copy of the license and copyright notice must be included with the licensed material.",
                            "Name": "License and copyright notice"
                        },
                        {
                            "Description": "Changes made to the licensed material must be documented.",
                            "Name": "State changes"
                        }
                    ],
                    "Content": "                                 Apache License\n                           Version 2.0, January 2004\n",
                    "ForbiddenSet": [
                        {
                            "Description": "This license explicitly states that it does NOT grant trademark rights, even though licenses without such a statement probably do not grant any implicit trademark rights.",
                            "Name": "Trademark use"
                        },
                        {
                            "Description": "This license includes a limitation of liability.",
                            "Name": "Liability"
                        },
                        {
                            "Description": "This license explicitly states that it does NOT provide any warranty.",
                            "Name": "Warranty"
                        }
                    ],
                    "PermissionSet": [
                        {
                            "Description": "The licensed material and derivatives may be used for commercial purposes.",
                            "Name": "Commercial use"
                        },
                        {
                            "Description": "The licensed material may be modified.",
                            "Name": "Modification"
                        },
                        {
                            "Description": "The licensed material may be distributed.",
                            "Name": "Distribution"
                        },
                        {
                            "Description": "This license explicitly states that it does NOT grant any rights in the patents of contributors.",
                            "Name": "Patent use"
                        },
                        {
                            "Description": "The licensed material may be used and modified in private.",
                            "Name": "Private use"
                        }
                    ]
                },
                "LicenseSummary": {
                    "Key": "apache-2.0",
                    "Name": "Apache License 2.0",
                    "Risk": "MediumRisk",
                    "SPDXKey": "Apache-2.0",
                    "ShortName": "Apache 2.0",
                    "Source": "https://spdx.org/licenses/Apache-2.0.html"
                }
            }
        ],
        "NormalizedLicenseExpression": "apache-2.0",
        "RequestId": "26112148-876a-4bc7-a427-1985371c65fd"
    }
}
```

