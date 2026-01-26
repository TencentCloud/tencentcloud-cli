**Example 1: 查询50条资源，无过滤条件**



Input: 

```
tccli cloudrc ListResources --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --Cursor 0 \
    --PageSize 50
```

Output: 
```
{
    "Response": {
        "Cursor": null,
        "List": [
            {
                "CreateTime": "2023-02-17 06:46:53",
                "PayMode": 0,
                "PrivateIpAddress": null,
                "ProductKey": "cam::cvm::volume",
                "PublicIpAddress": null,
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ResourceAlias": "Test_数据盘_1",
                "ResourceId": "disk-k8ujkh6s",
                "ResourceUniqueId": "wEBzkwyAXsCj8jJBN4MLtw==",
                "Uin": 123456789,
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2"
            }
        ],
        "RequestId": "766726d6-96c9-492e-a82d-f08c19aadcae"
    }
}
```

**Example 2: 查询云服务器实例资源，且镜像ID为"img-3la7wgnt"或"img-3la7wgnb"的资源，且实例规格"S2"**



Input: 

```
tccli cloudrc ListResources --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ConditionRule.Type complex \
    --ConditionRule.ComplexOption and \
    --ConditionRule.ComplexArray.0.SimpleKey ProductKey \
    --ConditionRule.ComplexArray.0.SimpleOption equals \
    --ConditionRule.ComplexArray.0.SimpleValue cam::cvm::instance \
    --ConditionRule.ComplexArray.0.Type simple \
    --ConditionRule.ComplexArray.1.SimpleKey ImageId \
    --ConditionRule.ComplexArray.1.SimpleValue img-3la7wgnt \
    --ConditionRule.ComplexArray.1.SimpleOption equals \
    --ConditionRule.ComplexArray.1.Type simple \
    --ConditionRule.ComplexArray.2.SimpleKey InstanceType \
    --ConditionRule.ComplexArray.2.SimpleValue S2 \
    --ConditionRule.ComplexArray.2.SimpleOption contains \
    --ConditionRule.ComplexArray.2.Type simple \
    --Cursor 0 \
    --PageSize 30
```

Output: 
```
{
    "Response": {
        "Cursor": null,
        "List": [
            {
                "ResourceUniqueId": "fhZp2lAMF7VFvDzlfxjPOw==",
                "ResourceId": "ins-wq8phzdh",
                "ResourceAlias": "Test0",
                "Uin": 123456789,
                "ProductKey": "cam::cvm::instance",
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2",
                "PayMode": 0,
                "PrivateIpAddress": "172.16.0.4",
                "PublicIpAddress": "",
                "CreateTime": "2023-02-17 06:47:14"
            },
            {
                "ResourceUniqueId": "DU8H4f/cUDBRzdHmK7Y1zA==",
                "ResourceId": "ins-wq8v2yl7",
                "ResourceAlias": "Test1",
                "Uin": 123456789,
                "ProductKey": "cam::cvm::instance",
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2",
                "PayMode": 0,
                "PrivateIpAddress": "172.16.0.16",
                "PublicIpAddress": "",
                "CreateTime": "2023-02-17 08:47:10"
            }
        ],
        "RequestId": "c39965b0-5f2d-4a5e-b12b-4906c37549bc"
    }
}
```

**Example 3: 查询地域为华东地区（上海）或可用区为广州二区的资源**



Input: 

```
tccli cloudrc ListResources --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ConditionRule.ComplexArray.0.Type simple \
    --ConditionRule.ComplexArray.0.SimpleKey RegionId \
    --ConditionRule.ComplexArray.0.SimpleOption equals \
    --ConditionRule.ComplexArray.0.SimpleValue 4 \
    --ConditionRule.ComplexArray.1.Type simple \
    --ConditionRule.ComplexArray.1.SimpleKey ZoneId \
    --ConditionRule.ComplexArray.1.SimpleOption equals \
    --ConditionRule.ComplexArray.1.SimpleValue 100002 \
    --ConditionRule.ComplexOption or \
    --ConditionRule.Type complex \
    --Cursor 0 \
    --PageSize 30
```

Output: 
```
{
    "Response": {
        "Cursor": null,
        "List": [
            {
                "ResourceUniqueId": "dxdBvR4OcRwV9dEv8/G5VA==",
                "ResourceId": "disk-k8utmh6s",
                "ResourceAlias": "Test0",
                "Uin": 123456789,
                "ProductKey": "cam::cvm::volume",
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2",
                "PayMode": 0,
                "PrivateIpAddress": null,
                "PublicIpAddress": null,
                "CreateTime": "2023-02-17 06:46:53"
            },
            {
                "ResourceUniqueId": "fhZp2lAMF7VFvDzlfxjPOw==",
                "ResourceId": "ins-wq8phzdh",
                "ResourceAlias": "Test1",
                "Uin": 123456789,
                "ProductKey": "cam::cvm::instance",
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2",
                "PayMode": 0,
                "PrivateIpAddress": "172.16.0.4",
                "PublicIpAddress": "",
                "CreateTime": "2023-02-17 06:47:14"
            }
        ],
        "RequestId": "9fb325e0-3571-4874-b9a9-e8988db369e3"
    }
}
```

**Example 4: 查询资源名称包含"Test"、且可用区为广州二区、且产品为云硬盘和云服务器实例、且标记了"部门"="开发部"标签、且计费模式为后付费的资源**



Input: 

```
tccli cloudrc ListResources --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ConditionRule.Type complex \
    --ConditionRule.ComplexOption and \
    --ConditionRule.ComplexArray.0.SimpleKey ResourceAlias \
    --ConditionRule.ComplexArray.0.SimpleValue Test \
    --ConditionRule.ComplexArray.0.SimpleOption contains \
    --ConditionRule.ComplexArray.0.Type simple \
    --ConditionRule.ComplexArray.1.Type simple \
    --ConditionRule.ComplexArray.1.SimpleKey ZoneId \
    --ConditionRule.ComplexArray.1.SimpleOption equals \
    --ConditionRule.ComplexArray.1.SimpleValue 100002 \
    --ConditionRule.ComplexArray.2.SimpleKey ProductKey \
    --ConditionRule.ComplexArray.2.SimpleValue cam::cvm::volume cam::cvm::instance \
    --ConditionRule.ComplexArray.2.SimpleOption equals \
    --ConditionRule.ComplexArray.2.Type simple \
    --ConditionRule.ComplexArray.3.Type simple \
    --ConditionRule.ComplexArray.3.SimpleKey tag:部门 \
    --ConditionRule.ComplexArray.3.SimpleOption equals \
    --ConditionRule.ComplexArray.3.SimpleValue 开发部 \
    --ConditionRule.ComplexArray.4.SimpleKey PayMode \
    --ConditionRule.ComplexArray.4.SimpleValue 0 \
    --ConditionRule.ComplexArray.4.SimpleOption equals \
    --ConditionRule.ComplexArray.4.Type simple \
    --Cursor 0 \
    --PageSize 30
```

Output: 
```
{
    "Response": {
        "Cursor": null,
        "List": [
            {
                "ResourceUniqueId": "SkfYG8haWEhE4IMblcYqqw==",
                "ResourceId": "ins-wuejtzp8",
                "ResourceAlias": "Test0_系统盘",
                "Uin": 123456789,
                "ProductKey": "cam::cvm::instance",
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2",
                "PayMode": 0,
                "PrivateIpAddress": null,
                "PublicIpAddress": null,
                "CreateTime": "2023-05-09 17:42:33"
            },
            {
                "ResourceUniqueId": "81UI4lAGkbFIPHploVYZTg==",
                "ResourceId": "disk-9yose6ro",
                "ResourceAlias": "Test1_系统盘",
                "Uin": 123456789,
                "ProductKey": "cam::cvm::volume",
                "RegionId": 1,
                "RegionCode": "ap-guangzhou",
                "ZoneId": 100002,
                "ZoneCode": "ap-guangzhou-2",
                "PayMode": 0,
                "PrivateIpAddress": null,
                "PublicIpAddress": null,
                "CreateTime": "2023-05-09 17:42:09"
            }
        ],
        "RequestId": "2773ef2c-d9da-4fbd-930d-f60a42ef4508"
    }
}
```

