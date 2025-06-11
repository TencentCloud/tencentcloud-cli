**Example 1: 产品列表**



Input: 

```
tccli cloudrc ListProducts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ProductCategory": "clb",
                "ProductKey": "cam::clb::clb",
                "ProductPrimaryName": "负载均衡",
                "ProductSecondaryName": "负载均衡实例",
                "ProductCategoryIconUrl": "https://cloudcache.tencentcs.com/qcloud/ui/static/cloud_prod_dict/2039/3d/light.png",
                "ConsoleUrlFormat": "/clb/detail?rid=${RegionId}&id=${ResourceId}",
                "BusinessFields": [
                    {
                        "Key": "ZoneId",
                        "Name": "可用区",
                        "Description": null,
                        "Unit": null,
                        "Type": "int",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "ResourceId",
                        "Name": "资源ID",
                        "Description": null,
                        "Unit": null,
                        "Type": "string",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "ResourceAlias",
                        "Name": "资源名称",
                        "Description": null,
                        "Unit": null,
                        "Type": "string",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals",
                            "contains",
                            "not_contains"
                        ]
                    },
                    {
                        "Key": "RegionId",
                        "Name": "地域",
                        "Description": null,
                        "Unit": null,
                        "Type": "int",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "ResourceUniqueId",
                        "Name": "资源唯一ID",
                        "Description": null,
                        "Unit": null,
                        "Type": "int",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "PayMode",
                        "Name": "计费模式",
                        "Description": null,
                        "Unit": null,
                        "Type": "enum",
                        "EnumDefine": [
                            {
                                "Name": "后付费",
                                "Value": "0"
                            },
                            {
                                "Name": "预付费",
                                "Value": "1"
                            },
                            {
                                "Name": "预留实例",
                                "Value": "2"
                            }
                        ],
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "Vip",
                        "Name": "VIP",
                        "Description": null,
                        "Unit": null,
                        "Type": "string",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "LoadBalancerType",
                        "Name": "实例类型",
                        "Description": null,
                        "Unit": null,
                        "Type": "enum",
                        "EnumDefine": [
                            {
                                "Name": "公网",
                                "Value": "open"
                            },
                            {
                                "Name": "内网",
                                "Value": "internal"
                            }
                        ],
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "MaxBandwidth",
                        "Name": "带宽上限",
                        "Description": null,
                        "Unit": "Mbps",
                        "Type": "int",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "VpcId",
                        "Name": "VPC ID",
                        "Description": null,
                        "Unit": null,
                        "Type": "string",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "PrivateIpAddress",
                        "Name": "内网IP",
                        "Description": null,
                        "Unit": null,
                        "Type": "string",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    {
                        "Key": "PublicIpAddress",
                        "Name": "外网IP",
                        "Description": null,
                        "Unit": null,
                        "Type": "string",
                        "EnumDefine": null,
                        "SupportedSimpleOption": [
                            "equals",
                            "not_equals"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "7af3420f-1da8-466a-aea9-57d57518dcf8"
    }
}
```

