**Example 1: 示例**

查询用户所有云服务器已有地域的地域列表

Input: 

```
tccli cwp DescribeMachineRegionList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionList": [
            {
                "MachineType": "ALL",
                "CloudFrom": 0,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-guangzhou-ecm-cm2",
                        "RegionName": "华南（广州移动2）",
                        "RegionId": 1063,
                        "RegionCode": "ap-guangzhou-ecm-cm2",
                        "RegionNameEn": "china-south（ap-guangzhou-ecm-cm2）"
                    },
                    {
                        "Region": "ap-beijing-ecm-cm3",
                        "RegionName": "华北（北京移动3）",
                        "RegionId": 1058,
                        "RegionCode": "ap-beijing-ecm-cm3",
                        "RegionNameEn": "china-north（ap-beijing-ecm-cm3）"
                    },
                    {
                        "Region": "ap-nanjing",
                        "RegionName": "华东地区（南京）",
                        "RegionId": 33,
                        "RegionCode": "nj",
                        "RegionNameEn": "East China (Nanjing)"
                    }
                ]
            },
            {
                "MachineType": "LH",
                "CloudFrom": 0,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-beijing",
                        "RegionName": "华北地区 (北京)",
                        "RegionId": 8,
                        "RegionCode": "bj",
                        "RegionNameEn": "North China (Beijing)"
                    },
                    {
                        "Region": "ap-guangzhou",
                        "RegionName": "华南地区 (广州)",
                        "RegionId": 1,
                        "RegionCode": "gz",
                        "RegionNameEn": "South China (Guangzhou)"
                    },
                    {
                        "Region": "ap-shanghai",
                        "RegionName": "华东地区 (上海)",
                        "RegionId": 4,
                        "RegionCode": "sh",
                        "RegionNameEn": "East China (Shanghai)"
                    }
                ]
            },
            {
                "MachineType": "Other",
                "CloudFrom": 1,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-others",
                        "RegionName": "其他地域（其他）",
                        "RegionId": 47,
                        "RegionCode": "others",
                        "RegionNameEn": "Others (Other)"
                    }
                ]
            },
            {
                "MachineType": "Other",
                "CloudFrom": 0,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-others",
                        "RegionName": "其他地域（其他）",
                        "RegionId": 47,
                        "RegionCode": "others",
                        "RegionNameEn": "Others (Other)"
                    }
                ]
            },
            {
                "MachineType": "ECM",
                "CloudFrom": 0,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-guangzhou-ecm-cm2",
                        "RegionName": "华南（广州移动2）",
                        "RegionId": 1063,
                        "RegionCode": "ap-guangzhou-ecm-cm2",
                        "RegionNameEn": "china-south（ap-guangzhou-ecm-cm2）"
                    }
                ]
            },
            {
                "MachineType": "EKS-NATIVE",
                "CloudFrom": 0,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-beijing",
                        "RegionName": "华北地区（北京）",
                        "RegionId": 8,
                        "RegionCode": "bj",
                        "RegionNameEn": "North China (Beijing)"
                    }
                ]
            },
            {
                "MachineType": "CVM",
                "CloudFrom": 0,
                "RegionList": [
                    {
                        "Region": "all-regions",
                        "RegionName": "全地域",
                        "RegionId": 999,
                        "RegionCode": "all",
                        "RegionNameEn": "All regions"
                    },
                    {
                        "Region": "ap-guangzhou",
                        "RegionName": "华南地区（广州）",
                        "RegionId": 1,
                        "RegionCode": "gz",
                        "RegionNameEn": "South China (Guangzhou)"
                    }
                ]
            }
        ],
        "RequestId": "94245821-efb0-4220-a909-6b58888e2ffe"
    }
}
```

