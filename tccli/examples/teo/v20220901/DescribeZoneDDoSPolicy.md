**Example 1: 查询所有防护分区**



Input: 

```
tccli teo DescribeZoneDDoSPolicy --cli-unfold-argument  \
    --ZoneId zone-xxqr76cy
```

Output: 
```
{
    "Response": {
        "RequestId": "68b3b15b-92e5-4136-9c27-4b892b1606fb",
        "DDoSHosts": [],
        "ShieldAreas": []
    }
}
```

