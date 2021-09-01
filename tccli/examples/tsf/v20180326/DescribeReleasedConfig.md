**Example 1: 查询group发布的配置**



Input: 

```
tccli tsf DescribeReleasedConfig --cli-unfold-argument  \
    --GroupId group-qv382dy7
```

Output: 
```
{
    "Response": {
        "RequestId": "2f65737d-7707-43b7-b024-b8aff844ab8f",
        "Result": "spring:\n  servlet:\n    multipart:\n      max-file-size: 100MB\n      max-request-size: 100MB\n  jackson:\n    serialization:\n      write-dates-as-timestamps: true\n  data:\n    mongodb:\n      uri: mongodb://commentuser:9xa#Lkp6sT@10.10.11.13:27017/comment\n  dubbo:\n    registry:\n      protocol: dubbo\n      address: tsfconsul://169.254.0.77:8000\n  datasource:\n    url: jdbc:mysql:replication://10.10.2.148:3306,10.10.2.148:3306,10.10.2.148:3306/rrmj2?roundRobinLoadBalance=true\n    username: rrtvappuser\n  "
    }
}
```

