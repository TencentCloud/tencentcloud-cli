**Example 1: 查询全地域实例数量**

查询全地域实例数量

Input: 

```
tccli lighthouse DescribeAllResourcesCount --cli-unfold-argument  \
    --ResourceNames INSTANCE
```

Output: 
```
{
    "Response": {
        "RequestId": "f818021e-d2ed-43b5-882d-390d54f807f5",
        "ResourcesCountSet": [
            {
                "ErrorCode": "",
                "Region": "ap-guangzhou",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-shanghai",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-hongkong",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-beijing",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-singapore",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "na-siliconvalley",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-chengdu",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-tokyo",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-nanjing",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-mumbai",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "eu-frankfurt",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "na-toronto",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-seoul",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "ap-jakarta",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            },
            {
                "ErrorCode": "",
                "Region": "sa-saopaulo",
                "ResourceCountDetailSet": [
                    {
                        "ResourceCount": 382,
                        "ResourceName": "INSTANCE"
                    }
                ]
            }
        ]
    }
}
```

