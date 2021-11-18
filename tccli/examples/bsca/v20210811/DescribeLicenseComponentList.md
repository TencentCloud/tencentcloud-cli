**Example 1: 查询含有风险License的组件列表**



Input: 

```
tccli bsca DescribeLicenseComponentList --cli-unfold-argument  \
    --AnalysisId f4461442-be34-4c60-ab21-55860baa9940 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ComponentSet": [
            {
                "Name": "apex",
                "Description": " The APEX Boot Loader is a modular and retargetable firmware loader\n suitable for embedded systems.\n .\n This package is a version of APEX configured for the Linksys NSLU2\n network appliance.  In this case, APEX is used as a second stage\n loader so that Redboot, as installed by the manufacturer, may remain.\n .\n The APEX command line offers a comfortable (e.g. command line editing\n and history) and extensible platform for development and production\n uses.\n .\n <http://wiki.buici.com/wiki/Apex_Bootloader>\n",
                "LicenseInfoSet": [
                    {
                        "Name": "GPL-2.0",
                        "Risk": "HighRisk"
                    }
                ]
            },
            {
                "Name": "arptables",
                "Description": "The arptables is a user space tool used to set up and maintain\nthe tables of ARP rules in the Linux kernel. These rules inspect\nthe ARP frames which they see. arptables is analogous to the iptables\nuser space tool, but is less complicated.",
                "LicenseInfoSet": [
                    {
                        "Name": "GPL-2.0",
                        "Risk": "HighRisk"
                    }
                ]
            }
        ],
        "FieldValuesSet": [
            {
                "Field": "Risk",
                "Values": [
                    "HighRisk",
                    "LowRisk",
                    "MiddleRisk"
                ]
            }
        ],
        "TotalCount": 30,
        "RequestId": "dab9fa49-083a-409a-88d8-c70b7df3925b"
    }
}
```

