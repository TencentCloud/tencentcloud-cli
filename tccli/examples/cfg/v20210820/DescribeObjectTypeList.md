**Example 1: 请求对象类型列表**



Input: 

```
tccli cfg DescribeObjectTypeList --cli-unfold-argument  \
    --SupportType 1
```

Output: 
```
{
    "Response": {
        "ObjectTypeList": [
            {
                "ArchLayer": 2,
                "ObjectHasNewAction": false,
                "ObjectPlatformName": "CVM",
                "ObjectSupportType": 2,
                "ObjectTypeId": 1,
                "ObjectTypeJsonParse": null,
                "ObjectTypeLevelOne": "计算",
                "ObjectTypeParams": {
                    "Fields": [
                        {
                            "Header": "实例ID",
                            "JsonParse": null,
                            "Key": "InstanceId",
                            "Transfer": null,
                            "Type": 0
                        },
                        {
                            "Header": "实例名称",
                            "JsonParse": null,
                            "Key": "InstanceName",
                            "Transfer": null,
                            "Type": 0
                        },
                        {
                            "Header": "可用区",
                            "JsonParse": null,
                            "Key": "Placement.Zone",
                            "Transfer": "{\"ap-seoul-1\": \"\\u9996\\u5c14\\u4e00\\u533a\", \"ap-seoul-2\": \"\\u9996\\u5c14\\u4e8c\\u533a\"}",
                            "Type": 0
                        },
                        {
                            "Header": "主IPv4地址",
                            "JsonParse": null,
                            "Key": "PrivateIpAddresses",
                            "Transfer": null,
                            "Type": 0
                        },
                        {
                            "Header": "VPC-ID",
                            "JsonParse": null,
                            "Key": "VirtualPrivateCloud.VpcId",
                            "Transfer": null,
                            "Type": 0
                        },
                        {
                            "Header": "子网ID",
                            "JsonParse": null,
                            "Key": "VirtualPrivateCloud.SubnetId",
                            "Transfer": null,
                            "Type": 0
                        }
                    ],
                    "Key": "InstanceId"
                },
                "ObjectTypeTitle": "CVM"
            }
        ],
        "RequestId": "fd1309c8-f198-4a6e-924c-89a80a274138"
    }
}
```

