**Example 1: DescribeInstanceLoginInfo**



Input: 

```
tccli cynosdb DescribeInstanceLoginInfo --cli-unfold-argument  \
    --InstanceId cynosdbmysql-xxx \
    --ResourceId cynosdbmysql-ins-xxx
```

Output: 
```
{
    "Response": {
        "InstanceId": "cynosdbmysql-xxx",
        "Items": [
            {
                "VpcId": "abc",
                "SubnetId": "abc",
                "VIP": "abc",
                "VPort": 0,
                "Region": "abc",
                "Zone": "abc",
                "Type": "abc",
                "Status": "abc",
                "ResourceId": "abc",
                "ResourceName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

