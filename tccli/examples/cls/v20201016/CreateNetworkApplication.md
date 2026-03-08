**Example 1: 创建网络应用**

用于创建网络应用

Input: 

```
tccli cls CreateNetworkApplication --cli-unfold-argument  \
    --Name network_application_demo \
    --LogsetId 0af7e6bb-fc91-4ee8-ad24-1129e9c91c6c \
    --TopicName network_application_demo1
```

Output: 
```
{
    "Response": {
        "NetworkAppId": "c902ffc9-48ad-40b1-9ef0-0bce45c050c2",
        "RequestId": "24339c03-22ee-4399-a1ba-fcf74807e769"
    }
}
```

