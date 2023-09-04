**Example 1: 默认查询条件**

仅查询BGP IP库存

Input: 

```
tccli vpc DescribeAddressAvailability --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AvailabilitySet": [
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "ap-guangzhou-1",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "ap-guangzhou-2",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "ap-guangzhou-3",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "ap-guangzhou-4",
                "NetworkGroup": "ap-guangzhou"
            }
        ],
        "RequestId": "81a1d693-b83c-4412-a108-4abcbc28d025"
    }
}
```

**Example 2: 查询全部可申请IP库存**



Input: 

```
tccli vpc DescribeAddressAvailability --cli-unfold-argument  \
    --AllPossibleCombinations TRUE
```

Output: 
```
{
    "Response": {
        "AvailabilitySet": [
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "ap-guangzhou-2",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "ap-guangzhou-3",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Unavailable",
                "InternetServiceProvider": "CMCC",
                "Zone": "ap-guangzhou-2",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Unavailable",
                "InternetServiceProvider": "CMCC",
                "Zone": "ap-guangzhou-3",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Unavailable",
                "InternetServiceProvider": "CUCC",
                "Zone": "ap-guangzhou-2",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Unavailable",
                "InternetServiceProvider": "CUCC",
                "Zone": "ap-guangzhou-3",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "CTCC",
                "Zone": "ap-guangzhou-2",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "EIP",
                "ResourceType": "",
                "Availability": "Available",
                "InternetServiceProvider": "CTCC",
                "Zone": "ap-guangzhou-3",
                "NetworkGroup": "ap-guangzhou"
            },
            {
                "AddressCount": 1,
                "AddressType": "AnycastEIP",
                "ResourceType": "ANYCAST_ZONE_GLOBAL",
                "Availability": "Available",
                "InternetServiceProvider": "BGP",
                "Zone": "",
                "NetworkGroup": "ap-guangzhou"
            }
        ],
        "RequestId": "7451d996-8814-468f-a469-262145574559"
    }
}
```

