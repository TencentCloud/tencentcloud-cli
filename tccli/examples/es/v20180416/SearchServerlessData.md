**Example 1: Serverless索引查询内部接口**

Serverless索引查询内部接口

Input: 

```
tccli es SearchServerlessData --cli-unfold-argument  \
    --ServerlessId index-35sj24o2 \
    --Host 10.0.0.84 10.0.0.1 \
    --LogPath /root/filebeat-7.14.2-linux-x86_64/access.log \
    --From 1609905184000 \
    --To 1679905184000 \
    --Query * \
    --Username cdw-filebeat \
    --Password 123456*
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "RequestId": "828f306d-cc86-11ed-bc7c-5254005fab95",
        "Results": [],
        "SearchAfterKeyFirst": null,
        "SearchAfterKeyLast": null
    }
}
```

