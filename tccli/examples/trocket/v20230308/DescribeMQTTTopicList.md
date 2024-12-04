**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTTopicList --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "InstanceId": "mqtt-47ka4rdr",
                "Remark": "this is remark",
                "Topic": "topic2"
            },
            {
                "InstanceId": "mqtt-47ka4rdr",
                "Remark": "this is remark",
                "Topic": "topic24"
            },
            {
                "InstanceId": "mqtt-47ka4rdr",
                "Remark": "this is remark",
                "Topic": "topic23"
            }
        ],
        "RequestId": "d9042e88-c70e-4158-958c-8bb57d6c809f",
        "TotalCount": 3
    }
}
```

