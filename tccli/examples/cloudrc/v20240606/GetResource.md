**Example 1: 查询资源详情**

查询资源详情

Input: 

```
tccli cloudrc GetResource --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ResourceUniqueId FWbAi7F/AulKZmxsA2mNOA==
```

Output: 
```
{
    "Response": {
        "ResourceUniqueId": "FWbAi7F/AulKZmxsA2mNOA==",
        "ResourceId": "ins-wxeo34kf",
        "ResourceAlias": "未命名",
        "Uin": 909619400,
        "ProductKey": "cam::cvm::instance",
        "RegionId": 1,
        "ZoneId": 100002,
        "PayMode": 1,
        "CreateTime": "2023-07-08 02:54:33",
        "BusinessFields": [
            {
                "Key": "PublicIpAddress",
                "Name": "外网IP",
                "Description": null,
                "Unit": null,
                "Type": "string",
                "Value": "",
                "ValueEnumName": null
            },
            {
                "Key": "ImageName",
                "Name": "镜像名称",
                "Description": null,
                "Unit": null,
                "Type": "string",
                "Value": "tlinux3.1x86_64",
                "ValueEnumName": null
            },
            {
                "Key": "PrivateIpAddress",
                "Name": "内网IP",
                "Description": null,
                "Unit": null,
                "Type": "string",
                "Value": "10.12.0.22",
                "ValueEnumName": null
            },
            {
                "Key": "PublicNetworkBandwidth",
                "Name": "公网带宽",
                "Description": null,
                "Unit": "Mbps",
                "Type": "int",
                "Value": "0",
                "ValueEnumName": null
            },
            {
                "Key": "SystemDiskSize",
                "Name": "系统盘容量",
                "Description": null,
                "Unit": "GiB",
                "Type": "int",
                "Value": null,
                "ValueEnumName": null
            },
            {
                "Key": "Memory",
                "Name": "内存",
                "Description": null,
                "Unit": "GB",
                "Type": "int",
                "Value": "4",
                "ValueEnumName": null
            },
            {
                "Key": "ImageId",
                "Name": "镜像ID",
                "Description": null,
                "Unit": null,
                "Type": "string",
                "Value": "img-eb30mz89",
                "ValueEnumName": null
            },
            {
                "Key": "NetworkBillingMode",
                "Name": "网络计费模式",
                "Description": null,
                "Unit": null,
                "Type": "enum",
                "Value": "1",
                "ValueEnumName": "包年/包月"
            },
            {
                "Key": "Cpu",
                "Name": "CPU",
                "Description": null,
                "Unit": "核",
                "Type": "int",
                "Value": "2",
                "ValueEnumName": null
            },
            {
                "Key": "InstanceType",
                "Name": "实例规格",
                "Description": null,
                "Unit": null,
                "Type": "string",
                "Value": "S2.MEDIUM4",
                "ValueEnumName": null
            }
        ],
        "Tags": [
            {
                "Key": "project",
                "Value": "默认项目"
            }
        ],
        "RequestId": "2138d26f-fe46-4eb3-a0f6-fb3d86be3389"
    }
}
```

**Example 2: 查询的资源不存在**

查询的资源不存在

Input: 

```
tccli cloudrc GetResource --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ResourceUniqueId ZlIFm+oOQ3jLgwR3txrMYA==
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ResourceIdNotFound",
            "Message": "资源ID不存在"
        },
        "RequestId": "2138d26f-fe46-4eb3-a0f6-fb3d86be3389"
    }
}
```

