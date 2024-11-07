**Example 1: 查询支持的HSM类型**

查询支持的HSM类型

Input: 

```
tccli cloudhsm DescribeSupportedHsm --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DeviceTypes": [
            {
                "HsmTypes": [
                    {
                        "HsmType": "EHSM",
                        "Model": "TASS CRYPTO ENGINE",
                        "VsmTypes": [
                            {
                                "TypeID": 15,
                                "TypeName": "EHSM"
                            }
                        ]
                    },
                    {
                        "HsmType": "SHSM",
                        "Model": "TASS CRYPTO ENGINE",
                        "VsmTypes": [
                            {
                                "TypeID": 47,
                                "TypeName": "SHSM"
                            }
                        ]
                    },
                    {
                        "HsmType": "GHSM",
                        "Model": "TASS CRYPTO ENGINE",
                        "VsmTypes": [
                            {
                                "TypeID": 31,
                                "TypeName": "GHSM"
                            }
                        ]
                    },
                    {
                        "HsmType": "virtualization",
                        "Model": "SJJ1528",
                        "VsmTypes": [
                            {
                                "TypeID": 49,
                                "TypeName": "SVSM"
                            },
                            {
                                "TypeID": 17,
                                "TypeName": "EVSM"
                            },
                            {
                                "TypeID": 33,
                                "TypeName": "GVSM"
                            }
                        ]
                    }
                ],
                "Manufacturer": "TASS"
            },
            {
                "HsmTypes": [
                    {
                        "HsmType": "virtualization",
                        "Model": "SJJ1601",
                        "VsmTypes": [
                            {
                                "TypeID": 149,
                                "TypeName": "SVSM"
                            },
                            {
                                "TypeID": 117,
                                "TypeName": "EVSM"
                            },
                            {
                                "TypeID": 133,
                                "TypeName": "GVSM"
                            }
                        ]
                    }
                ],
                "Manufacturer": "SANSEC"
            }
        ],
        "RequestId": "59aa770a-4aba-429f-a8a1-646f98419f9d"
    }
}
```

