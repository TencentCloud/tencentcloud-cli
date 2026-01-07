**Example 1: 一般场景**

一般场景。

Input: 

```
tccli vpc DescribeAddressAssociationQuota --cli-unfold-argument  \
    --InstanceIds ins-19016fl4
```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "INSTANCE_ADDRESS_ASSOCIATION",
                "InstanceId": "ins-19016fl4",
                "QuotaCurrent": 1,
                "NetworkInterfaceId": "",
                "QuotaLimit": 3
            }
        ],
        "RequestId": "48da5ffc-d2a5-433d-b692-39e87a531e65"
    }
}
```

**Example 2: 升/降配场景**

升/降配场景。

Input: 

```
tccli vpc DescribeAddressAssociationQuota --cli-unfold-argument  \
    --CPU 2 \
    --InstanceIds ins-19016fl4 \
    --Memory 4
```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "INSTANCE_ADDRESS_ASSOCIATION",
                "InstanceId": "ins-19016fl4",
                "NetworkInterfaceId": "",
                "QuotaCurrent": -1,
                "QuotaLimit": 2
            }
        ],
        "RequestId": "b761b392-ad67-4499-9d03-04cdd056dabf"
    }
}
```

**Example 3: 无限制场景(仍然需要满足弹性网卡及内网IP配额限制)**

无限制场景(仍然需要满足弹性网卡及内网IP配额限制)。

Input: 

```
tccli vpc DescribeAddressAssociationQuota --cli-unfold-argument  \
    --InstanceIds ins-19016fl4
```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "INSTANCE_ADDRESS_ASSOCIATION",
                "InstanceId": "ins-19016fl4",
                "QuotaCurrent": -1,
                "QuotaLimit": -1,
                "NetworkInterfaceId": ""
            }
        ],
        "RequestId": "48da5ffc-d2a5-433d-b692-39e87a531e65"
    }
}
```

