**Example 1: Creating a VPC instance**



Input: 

```
tccli vpc CreateVpc --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcName TestVPC\
    --CidrBlock 10.8.0.0/16\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Vpc": {
            "VpcId": "vpc-4tboefn3",
            "VpcName": "TestVPC",
            "EnableMulticast": false,
            "CidrBlock": "10.8.0.0/16",
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ]
        }
    }
}
```

