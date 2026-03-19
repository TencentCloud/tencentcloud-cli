**Example 1: DescribeRPCMethodList**



Input: 

```
tccli cetcd DescribeRPCMethodList --cli-unfold-argument  \
    --InstanceId etcd-abcd1234 \
    --PodName etcd-abcd1234-etcd-0
```

Output: 
```
{
    "Response": {
        "MethodList": [
            {
                "Name": "Alarm"
            }
        ],
        "RequestId": "51abd77d-f503-41e7-ab28-010083e02a78"
    }
}
```

