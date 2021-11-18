**Example 1: 查询License详情**



Input: 

```
tccli bsca DescribeLicenseDetail --cli-unfold-argument  \
    --AnalysisId f4461442-be34-4c60-ab21-55860baa9940 \
    --ComponentName apex \
    --LicenseName GPL-2.0
```

Output: 
```
{
    "Response": {
        "License": {
            "Name": "GPL-2.0",
            "PermissionSet": [
                {
                    "Name": "Commercial Use",
                    "Description": "The licensed material and derivatives may be used for commercial purposes."
                },
                {
                    "Name": "Distribution",
                    "Description": "The licensed material may be distributed."
                },
                {
                    "Name": "Modification",
                    "Description": "The licensed material may be modified."
                },
                {
                    "Name": "Private Use",
                    "Description": "The licensed material may be used and modified in private."
                }
            ],
            "ConditionSet": [
                {
                    "Name": "Disclose Source",
                    "Description": "Source code must be made available when the licensed material is distributed."
                },
                {
                    "Name": "License and Copyright Notice",
                    "Description": "A copy of the license and copyright notice must be included with the licensed material."
                },
                {
                    "Name": "Same License",
                    "Description": "Modifications must be released under the same license when distributing the licensed material. In some cases a similar or related license may be used."
                },
                {
                    "Name": "Stage Changes",
                    "Description": "Changes made to the licensed material must be documented."
                }
            ],
            "ForbiddenSet": [
                {
                    "Name": "Liability",
                    "Description": "This license includes a limitation of liability."
                },
                {
                    "Name": "Warranty",
                    "Description": "This license explicitly states that it does NOT provide any warranty."
                }
            ],
            "Source": "https://opensource.org/licenses/GPL-2.0",
            "Content": "License Content"
        },
        "RequestId": "aee7ebf4-f91c-4a6c-be72-2d7fb10dfa4f"
    }
}
```

