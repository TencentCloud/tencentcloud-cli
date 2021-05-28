**Example 1: 查询支持的HSM类型**

查询支持的HSM类型

Input: 

```
tccli cloudhsm DescribeSupportedHsm --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "dafabf2e-9666-414c-9854-7f9584f9f656",
        "DeviceTypes": [
            {
                "Manufacturer": "江南天安",
                "HsmTypes": [
                    {
                        "Model": "SJJ1528",
                        "VsmTypes": [
                            {
                                "TypeName": "SVSM",
                                "TypeID": 49
                            },
                            {
                                "TypeName": "EVSM",
                                "TypeID": 17
                            },
                            {
                                "TypeName": "GVSM",
                                "TypeID": 33
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

