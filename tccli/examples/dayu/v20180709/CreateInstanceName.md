**Example 1: 资源实例重命名**



Input: 

```
tccli dayu CreateInstanceName --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Name 测试
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

