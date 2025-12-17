**Example 1: 权限点**



Input: 

```
tccli tccatalog GetGrantPrivilegesSTD --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "ManagePrivileges": [
                {
                    "Description": "u6240u6709u6743u9650uff08u4e0du5305u542bu7528u6237u548cu89d2u8272u7ba1u7406uff09",
                    "DescriptionEn": "The privilege to ALL but not contains User and role",
                    "Name": "ALL_PRIVILEGES"
                }
            ],
            "ResourcePrivileges": [
                {
                    "Description": "u4f7fu7528u6570u636eu76eeu5f55",
                    "DescriptionEn": "The privilege to use a catalog.",
                    "Name": "USE_CATALOG"
                }
            ],
            "ResourceType": "CATALOG",
            "SubResourcePrivileges": [
                {
                    "ManagePrivileges": [
                        {
                            "Description": "u6240u6709u6743u9650uff08u4e0du5305u542bu7528u6237u548cu89d2u8272u7ba1u7406uff09",
                            "DescriptionEn": "The privilege to ALL but not contains User and role",
                            "Name": "ALL_PRIVILEGES"
                        }
                    ],
                    "ResourceDependencyPrivileges": [
                        {
                            "Description": "u4f7fu7528u6570u636eu76eeu5f55",
                            "DescriptionEn": "The privilege to use a catalog.",
                            "Name": "USE_CATALOG"
                        }
                    ],
                    "ResourcePrivileges": [
                        {
                            "Description": "u4f7fu7528u6a21u5f0f",
                            "DescriptionEn": "The privilege to use a schema.",
                            "Name": "USE_SCHEMA"
                        }
                    ],
                    "ResourceType": "SCHEMA",
                    "SubResourcePrivileges": [
                        {
                            "ManagePrivileges": [
                                {
                                    "Description": "u6240u6709u6743u9650uff08u4e0du5305u542bu7528u6237u548cu89d2u8272u7ba1u7406uff09",
                                    "DescriptionEn": "The privilege to ALL but not contains User and role",
                                    "Name": "ALL_PRIVILEGES"
                                }
                            ],
                            "ResourceDependencyPrivileges": [
                                {
                                    "Description": "u4f7fu7528u6570u636eu76eeu5f55",
                                    "DescriptionEn": "The privilege to use a catalog.",
                                    "Name": "USE_CATALOG"
                                }
                            ],
                            "ResourcePrivileges": [
                                {
                                    "Description": "u4feeu6539u8868u6570u636eu6216u8868u7ed3u6784",
                                    "DescriptionEn": "The privilege to write data to a table or modify the table schema.",
                                    "Name": "MODIFY_TABLE"
                                }
                            ],
                            "ResourceType": "TABLE",
                            "SubResourcePrivileges": [
                                {
                                    "ManagePrivileges": [
                                        {
                                            "Description": "u6240u6709u6743u9650uff08u4e0du5305u542bu7528u6237u548cu89d2u8272u7ba1u7406uff09",
                                            "DescriptionEn": "The privilege to ALL but not contains User and role",
                                            "Name": "ALL_PRIVILEGES"
                                        }
                                    ],
                                    "ResourceDependencyPrivileges": [
                                        {
                                            "Description": "u4f7fu7528u6570u636eu76eeu5f55",
                                            "DescriptionEn": "The privilege to use a catalog.",
                                            "Name": "USE_CATALOG"
                                        }
                                    ],
                                    "ResourcePrivileges": [
                                        {
                                            "Description": "u9009u62e9u5217u6743u9650",
                                            "DescriptionEn": "The privilege to select column",
                                            "Name": "SELECT_COLUMN"
                                        }
                                    ],
                                    "ResourceType": "COLUMN"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "RequestId": "9c810898-108c-4ff5-941e-da6a93cef89c"
    }
}
```

