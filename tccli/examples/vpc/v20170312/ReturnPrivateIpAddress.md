**Example 1: 退还内网IP**

退还内网IP

Input: 

```
tccli vpc ReturnPrivateIpAddress --cli-unfold-argument  \
    --PrivateIpAddress “10.0.0.2” \
    --ResourceId tke-cls-3erfgt54 \
    --VpcId vpc-34edfr43
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

