**Example 1: 创建库**

创建一个demo库

Input: 

```
tccli cdwdoris CreateDatabase --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --DbName demo \
    --Properties.0.PropertyKey replication_allocation \
    --Properties.0.PropertyValue tag.location.default: 1
```

Output: 
```
{
    "Response": {
        "Message": "",
        "RequestId": "494d3ca4-1d4d-483a-b172-1fdd4acee042"
    }
}
```

